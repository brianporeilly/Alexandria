# Generated by Django 3.1.5 on 2021-01-29 05:08

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_form', models.CharField(blank=True, choices=[('datas', 'Dataset (digital content intended for processing)'), ('img', 'Image'), ('mvemt', 'Movement (content expressed through motion, i.e. dance)'), ('music', 'Music'), ('objct', 'Object (a physical, 3D object)'), ('progm', 'Program (software)'), ('sound', 'Sounds (sound effects, animal noises, etc.)'), ('spknw', 'Spoken Word'), ('text', 'Text'), ('mcf', 'Multiple Content Forms (three or more terms apply)'), ('ocf', 'Other Content Form')], default='text', help_text="What is this media? Select 'Multiple Media' if three or more types describe this media.", max_length=5, null=True)),
                ('content_qualification', models.CharField(blank=True, choices=[('carto', 'Cartographic'), ('notat', 'Notated'), ('perfo', 'Performed')], help_text='Optional', max_length=5, null=True)),
                ('sensory_type', models.CharField(blank=True, choices=[('aural', 'Aural'), ('gusta', 'Gustatory'), ('olfac', 'Olfactory'), ('tacti', 'Tactile'), ('visua', 'Visual')], help_text='Optional', max_length=5, null=True)),
                ('media_type', models.CharField(blank=True, choices=[('unmed', 'Unmediated'), ('audio', 'Audio'), ('elect', 'Electronic'), ('micfm', 'Microform'), ('micsp', 'Microscopic'), ('proje', 'Projected'), ('stero', 'Stereographic'), ('video', 'Video'), ('multm', 'Multiple Media'), ('othmd', 'Other Media')], default='unmed', help_text='Optional', max_length=5, null=True)),
                ('dimensionality', models.CharField(blank=True, choices=[('2d', '2-Dimensional'), ('3d', '3-Dimensional')], help_text='Optional -- image only', max_length=5, null=True)),
                ('motion_type', models.CharField(blank=True, choices=[('mvg', 'Moving'), ('still', 'Still')], help_text='Optional -- image only', max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContentTypeManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='primary_content_type', to='media.contenttype')),
                ('secondary', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secondary_content_type', to='media.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='ISBDRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('title_proper', models.TextField(blank=True, null=True)),
                ('title_parallel', models.TextField(blank=True, null=True)),
                ('title_information', models.TextField(blank=True, null=True)),
                ('title_statement_of_responsibility', models.TextField()),
                ('edition', models.TextField(blank=True, null=True)),
                ('specific_info', models.TextField(blank=True, null=True)),
                ('publisher', models.TextField(blank=True, null=True)),
                ('material_description', models.TextField(blank=True, null=True)),
                ('series', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('resource_identifier', models.TextField(blank=True, null=True)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('condition', models.CharField(blank=True, choices=[('new', 'New'), ('fine', 'Fine'), ('vygd', 'Very Good'), ('good', 'Good'), ('fair', 'Fair'), ('poor', 'Poor')], default='new', max_length=4, null=True)),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media.isbdrecord')),
                ('type', models.ManyToManyField(related_name='content_type', to='media.ContentTypeManager')),
            ],
        ),
    ]
