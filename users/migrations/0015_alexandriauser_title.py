# Generated by Django 3.2.9 on 2021-11-18 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0014_alter_alexandriauser_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="alexandriauser",
            name="title",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="title"
            ),
        ),
    ]
