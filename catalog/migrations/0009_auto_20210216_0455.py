# Generated by Django 3.1.5 on 2021-02-16 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20210216_0452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='catalog.itemtype'),
            preserve_default=False,
        ),
    ]
