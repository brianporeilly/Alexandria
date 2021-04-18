# Generated by Django 3.1.5 on 2021-03-08 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_record_summary'),
        ('holds', '0006_hold_requested_item_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hold',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='hold',
            name='object_id',
        ),
        migrations.AddField(
            model_name='hold',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.item'),
        ),
        migrations.AddField(
            model_name='hold',
            name='record',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.record'),
        ),
    ]