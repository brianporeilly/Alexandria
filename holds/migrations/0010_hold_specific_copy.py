# Generated by Django 3.2.8 on 2021-10-28 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holds', '0009_alter_hold_destination'),
    ]

    operations = [
        migrations.AddField(
            model_name='hold',
            name='specific_copy',
            field=models.BooleanField(default=False),
        ),
    ]