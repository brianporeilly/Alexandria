# Generated by Django 3.1.5 on 2021-02-18 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20210216_0455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.itemtype'),
        ),
    ]
