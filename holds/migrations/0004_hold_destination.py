# Generated by Django 3.1.5 on 2021-03-07 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_auto_20210208_0158"),
        ("holds", "0003_remove_hold_destination"),
    ]

    operations = [
        migrations.AddField(
            model_name="hold",
            name="destination",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.branchlocation",
            ),
            preserve_default=False,
        ),
    ]
