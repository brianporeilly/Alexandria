# Generated by Django 4.0 on 2022-01-08 06:35

import alexandria.searchablefields.mixins
import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BibliographicLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('a', 'Monographic component part'), ('b', 'Serial component part'), ('c', 'Collection'), ('d', 'Subunit'), ('i', 'Integrating resource'), ('m', 'Monograph / Item'), ('s', 'Serial')], max_length=1)),
                ('host', models.CharField(default='default', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('can_circulate', models.BooleanField(default=True)),
                ('host', models.CharField(default='default', max_length=100)),
                ('home', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.branchlocation')),
            ],
        ),
        migrations.CreateModel(
            name='ItemType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('number_of_days_per_checkout', models.IntegerField(blank=True, null=True)),
                ('number_of_allowed_renews', models.IntegerField(blank=True, null=True)),
                ('number_of_concurrent_checkouts', models.IntegerField(blank=True, null=True)),
                ('host', models.CharField(default='default', max_length=100)),
                ('icon_name', models.CharField(blank=True, help_text="The name of the Material Design icon that you'd like to display in the catalog for this type. https://fonts.google.com/icons?selected=Material+Icons", max_length=30, null=True, verbose_name='icon name')),
                ('icon_svg', models.TextField(blank=True, help_text='Don\'t have a matching option in the Material Design icons? Copy the full SVG html here to display that instead. WARNING: must be fully formed SVG element; it will not be saved otherwise. Make sure that your `path` tag has `fill="currentColor"` in it so that colors work correctly and ensure that it displays well as 36px by 36px.', null=True, verbose_name='icon svg')),
            ],
        ),
        migrations.CreateModel(
            name='ItemTypeBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('a', 'Language material'), ('c', 'Notated music'), ('d', 'Manuscript notated music'), ('e', 'Cartographic material'), ('f', 'Manuscript cartographic material'), ('g', 'Projected medium'), ('i', 'Nonmusical sound recording'), ('j', 'Musical sound recording'), ('k', 'Two-dimensional nonprojectable graphic'), ('m', 'Computer file'), ('o', 'Kit'), ('p', 'Mixed materials'), ('r', 'Three dimensional artifact or naturally occurring object'), ('t', 'Manuscript language material')], max_length=1)),
                ('host', models.CharField(default='default', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('host', models.CharField(default='default', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=26021)),
                ('authors', models.CharField(blank=True, max_length=500, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=26021, null=True)),
                ('uniform_title', models.CharField(blank=True, max_length=26021, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('series', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('summary', models.TextField(blank=True, null=True)),
                ('zenodotus_id', models.IntegerField(blank=True, null=True)),
                ('zenodotus_record_version', models.IntegerField(blank=True, null=True)),
                ('host', models.CharField(default='default', max_length=100)),
                ('searchable_title', models.CharField(max_length=26021)),
                ('searchable_authors', models.CharField(blank=True, max_length=500, null=True)),
                ('searchable_subtitle', models.CharField(blank=True, max_length=26021, null=True)),
                ('searchable_uniform_title', models.CharField(blank=True, max_length=26021, null=True)),
                ('bibliographic_level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='records.bibliographiclevel')),
                ('subjects', models.ManyToManyField(blank=True, to='records.Subject', verbose_name='list of subjects')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='records.itemtype')),
            ],
            bases=(models.Model, alexandria.searchablefields.mixins.SearchableFieldMixin),
        ),
        migrations.AddField(
            model_name='itemtype',
            name='base',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.itemtypebase'),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(blank=True, max_length=50, null=True, verbose_name='barcode')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='price')),
                ('condition', models.CharField(blank=True, choices=[('new', 'New'), ('fine', 'Fine'), ('vygd', 'Very Good'), ('good', 'Good'), ('fair', 'Fair'), ('poor', 'Poor')], default='new', max_length=4, null=True, verbose_name='condition')),
                ('is_active', models.BooleanField(default=False, help_text='Designates whether this piece of media is counted as part of the collection.', verbose_name='active')),
                ('isbn', models.CharField(blank=True, max_length=13, null=True, verbose_name='ISBN')),
                ('issn', models.CharField(blank=True, max_length=8, null=True, verbose_name='ISSN')),
                ('issn_title', models.TextField(blank=True, null=True, verbose_name='issn_title')),
                ('marc_location', models.TextField(blank=True, null=True, verbose_name='marc_location')),
                ('marc_leader', models.CharField(blank=True, max_length=50, null=True)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('call_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='call_number')),
                ('checkout_count', models.IntegerField(default=0, verbose_name='checkout_count')),
                ('sudoc', models.CharField(blank=True, max_length=30, null=True, verbose_name='sudoc')),
                ('last_checked_out', models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0, tzinfo=utc), verbose_name='last_checked_out')),
                ('can_circulate', models.BooleanField(default=True, verbose_name='can_circulate')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='notes')),
                ('physical_description', models.CharField(blank=True, max_length=500, null=True, verbose_name='physical_description')),
                ('publisher', models.CharField(max_length=500, verbose_name='publisher')),
                ('pubyear', models.IntegerField(blank=True, null=True, verbose_name='pubyear')),
                ('edition', models.CharField(blank=True, max_length=40, null=True, verbose_name='edition')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('due_date', models.DateField(default=datetime.datetime(1970, 1, 1, 0, 0), verbose_name='due_date')),
                ('renewal_count', models.IntegerField(default=0)),
                ('host', models.CharField(default='default', max_length=100)),
                ('bibliographic_level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='records.bibliographiclevel')),
                ('collection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='records.collection')),
                ('content_type', models.ForeignKey(blank=True, limit_choices_to={'model__in': ('branchlocation', 'alexandriauser')}, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('home_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.branchlocation')),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.record')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='records.itemtype')),
            ],
            options={
                'permissions': [('check_in', 'Can check in materials'), ('check_out', 'Can check out materials')],
            },
        ),
        migrations.CreateModel(
            name='Hold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('specific_copy', models.BooleanField(default=False)),
                ('force_next_available', models.BooleanField(default=False, help_text='Very rarely, certain holds need to be completed ahead of others. Setting this makes this hold be processed next, no matter where it is in the queue. If there are multiple holds with this flag, then they will be processed in order of oldest first.')),
                ('host', models.CharField(default='default', max_length=100)),
                ('destination', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.branchlocation')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='records.item')),
                ('placed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
