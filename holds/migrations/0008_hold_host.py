# Generated by Django 3.2.8 on 2021-10-26 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holds', '0007_auto_20210308_0610'),
    ]

    operations = [
        migrations.AddField(
            model_name='hold',
            name='host',
            field=models.CharField(default='default', max_length=100),
        ),
    ]
