from urllib.parse import quote_plus

from django.contrib.postgres.search import (
    SearchQuery,
    SearchRank,
    SearchVector,
    TrigramSimilarity,
)
from django.core.paginator import Paginator
from django.db.models.aggregates import Count
from django.db.models.expressions import F, Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse
from django.views.decorators.csrf import csrf_exempt

from alexandria.catalog.helpers import get_results_per_page
from alexandria.distributed.models import Setting
from alexandria.records.models import Record
from alexandria.users.helpers import add_patron_acted_as
from alexandria.utils.db import query_debugger
from alexandria.utils.type_hints import Request


@csrf_exempt
def index(request: Request) -> HttpResponse:
    if request.method == "POST":
        search_text = request.POST.get("search_text")
        return HttpResponseRedirect(
            reverse("search")
            + "?q="
            + ((quote_plus(search_text)) if search_text else "")
        )
    context = add_patron_acted_as(request, {})
    return render(request, "catalog/index.html", context)


@query_debugger
def search(request: Request) -> HttpResponse:
    context = dict()
    search_term = request.GET.get("q")
    if not search_term:
        return render(request, "catalog/search.html", context)
    ignored_terms = request.settings.get(
        Setting.options.IGNORED_SEARCH_TERMS, default=[]
    )
    if ignored_terms:
        ignored_terms = [term.strip() for term in ignored_terms.split(",")]

    search_term = " ".join([i for i in search_term.split() if i not in ignored_terms])
    # https://docs.djangoproject.com/en/4.0/ref/contrib/postgres/search/#searchrank
    # https://docs.djangoproject.com/en/4.0/ref/contrib/postgres/search/#searchvector
    # https://docs.djangoproject.com/en/4.0/ref/contrib/postgres/search/#trigram-similarity
    vector = (
        SearchVector("searchable_authors", weight="A")
        + SearchVector("searchable_title", weight="B")
        + SearchVector("searchable_uniform_title", weight="B")
        + SearchVector("searchable_subtitle", weight="C")
        + SearchVector("subjects__searchable_name", weight="C")
    )
    query = SearchQuery(search_term)
    results = (
        Record.objects.annotate(
            # NOTE! The TrigramSimilarity DOES NOT TAKE a SearchQuery! You must pass
            # in the actual raw search string. The resulting error message will be
            # that pg_trgm isn't installed, which is untrue. Thanks to @mcarlton00
            # for helping me get that figured out.
            author_similarity=TrigramSimilarity("searchable_authors", search_term),
            title_similarity=TrigramSimilarity("searchable_title", search_term),
            rank=SearchRank(vector, query),
        )
        .filter(
            Q(rank__gte=0.3)
            | Q(author_similarity__gte=0.3)
            | Q(title_similarity__gte=0.3),
            host=request.host,
            id__in=Record.objects.filter(item__isnull=False),
        )
        .exclude(
            id__in=(
                Record.objects.annotate(total_count=Count("item", distinct=True))
                .filter(item__is_active=False)
                .annotate(is_active=Count("item", distinct=True))
                .filter(Q(is_active=F("total_count")))
            )
        )
        .prefetch_related("type")
        .order_by("-rank")
        .distinct()
    )
    if not results:
        # Sometimes we'll get searches for things that are specific and shouldn't be
        # fuzzy. If it doesn't match above, see if the search is a barcode or call
        # number.
        results = Record.objects.filter(
            Q(item__barcode__icontains=search_term)
            | Q(item__call_number__icontains=search_term),
            host=request.host,
            item__is_active=True,
        ).order_by("-created_at")

    results_per_page = get_results_per_page(request)

    paginator = Paginator(results, results_per_page)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context.update(
        {"result_count": paginator.count, "results_per_page": results_per_page}
    )

    if search_term:
        context.update(
            {"search_term": search_term, "page": page_obj, "paginator": paginator}
        )
    context = add_patron_acted_as(request, context)
    return render(request, "catalog/search.html", context)


def item_detail(request, item_id):
    record = get_object_or_404(Record, id=item_id, host=request.host)
    context = add_patron_acted_as(request, {"record": record})
    return render(request, "catalog/item_detail.html", context)
