from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.utils.translation import ugettext as _
from django.views.generic import View

from catalog.models import Item
from holds.models import Hold
from users.forms import LoginForm, PatronSettingsForm
from utils import build_context
from utils.views import next_or_reverse


class LoginView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {"slim_form": True, "form": LoginForm, "show_password_reset": True}
        return render(request, "generic_form.html", context)

    def post(self, request: HttpRequest) -> HttpResponse:
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                int(data["card_number"])
            except ValueError:
                messages.error(
                    request, _("Card number needs to be the number on your card.")
                )
                return HttpResponseRedirect(next_or_reverse(request, "login"))

            user = authenticate(
                request, username=data["card_number"], password=data["password"]
            )
            if user and user.host == request.host:
                login(request, user)
                return HttpResponseRedirect(next_or_reverse(request, "homepage"))
            messages.error(request, _("Invalid login information. Try again?"))
            return HttpResponseRedirect(next_or_reverse(request, "login"))


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return HttpResponseRedirect(next_or_reverse(request, "homepage"))


def profile_settings(request: HttpRequest) -> HttpResponse:
    ...


def profile_settings_edit(request: HttpRequest) -> HttpResponse:
    ...


@login_required()
def my_checkouts(request: HttpRequest) -> HttpResponse:
    my_materials = Item.objects.filter(user_checked_out_to=request.user).order_by(
        "due_date"
    )
    return render(
        request, "user/my_checked_out.html", {"checkouts": my_materials}
    )


@login_required()
def my_holds(request: HttpRequest) -> HttpResponse:
    my_holds = Hold.objects.filter(placed_by=request.user, host=request.host)
    return render(request, "user/my_holds.html", {"holds": my_holds})


@login_required()
def my_fees(request: HttpRequest) -> HttpResponse:
    # TODO: Finish after building staff side
    my_fees = ...
    return render(request, "user/my_fees.html", {"fees": my_fees})


class SettingsView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
                "slim_form": True,
                "form": PatronSettingsForm(instance=request.user),
                "show_password_reset": True,
            }

        context.update({"header": _("My Settings")})
        return render(request, "generic_form.html", context)

    def post(self, request: HttpRequest) -> HttpResponse:
        form = PatronSettingsForm(request.POST, instance=request.user)
        fields = form.fields
        form.fields = {i: fields[i] for i in fields if i != "formatted_address"}
        if form.is_valid():
            form.save()
            messages.success(request, _("Your settings were updated!"))
            return redirect("my_settings")
