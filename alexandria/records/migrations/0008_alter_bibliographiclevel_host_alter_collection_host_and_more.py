# Generated by Django 4.0.5 on 2022-06-13 02:52

import alexandria.distributed.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("distributed", "0001_initial"),
        ("records", "0007_alter_checkoutsession_content_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bibliographiclevel",
            name="host",
            field=models.ForeignKey(
                default=alexandria.distributed.models.Domain.get_default_pk,
                on_delete=django.db.models.deletion.CASCADE,
                to="distributed.domain",
            ),
        ),
        migrations.AlterField(
            model_name="collection",
            name="host",
            field=models.ForeignKey(
                default=alexandria.distributed.models.Domain.get_default_pk,
                on_delete=django.db.models.deletion.CASCADE,
                to="distributed.domain",
            ),
        ),
        migrations.AlterField(
            model_name="hold",
            name="host",
            field=models.ForeignKey(
                default=alexandria.distributed.models.Domain.get_default_pk,
                on_delete=django.db.models.deletion.CASCADE,
                to="distributed.domain",
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="host",
            field=models.ForeignKey(
                default=alexandria.distributed.models.Domain.get_default_pk,
                on_delete=django.db.models.deletion.CASCADE,
                to="distributed.domain",
            ),
        ),
        migrations.AlterField(
            model_name="itemtype",
            name="host",
            field=models.ForeignKey(
                default=alexandria.distributed.models.Domain.get_default_pk,
                on_delete=django.db.models.deletion.CASCADE,
                to="distributed.domain",
            ),
        ),
        migrations.AlterField(
            model_name="itemtypebase",
            name="host",
            field=models.ForeignKey(
                default=alexandria.distributed.models.Domain.get_default_pk,
                on_delete=django.db.models.deletion.CASCADE,
                to="distributed.domain",
            ),
        ),
        migrations.AlterField(
            model_name="record",
            name="host",
            field=models.ForeignKey(
                default=alexandria.distributed.models.Domain.get_default_pk,
                on_delete=django.db.models.deletion.CASCADE,
                to="distributed.domain",
            ),
        ),
        migrations.AlterField(
            model_name="subject",
            name="host",
            field=models.ForeignKey(
                default=alexandria.distributed.models.Domain.get_default_pk,
                on_delete=django.db.models.deletion.CASCADE,
                to="distributed.domain",
            ),
        ),
    ]
