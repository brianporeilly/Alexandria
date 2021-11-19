# Generated by Django 3.2.9 on 2021-11-18 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0011_auto_20211115_1704"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="alexandriauser",
            options={
                "permissions": [
                    ("create_patron_account", "Can create a patron account"),
                    ("read_patron_account", "Can see patron account data"),
                    ("update_patron_account", "Can update patron account information"),
                    ("delete_patron_account", "Can delete patron accounts"),
                    ("edit_user_notes", "Can edit user notes field"),
                    ("create_staff_account", "Can create a staff account"),
                    ("read_staff_account", "Can see staff account data"),
                    ("update_staff_account", "Can update staff account information"),
                    ("delete_staff_account", "Can delete staff accounts"),
                    (
                        "generate_financial_reports",
                        "Can generate reports with financial data",
                    ),
                    (
                        "generate_general_reports",
                        "Can generate reports on anything non-financial",
                    ),
                ],
                "verbose_name": "user",
                "verbose_name_plural": "users",
            },
        ),
        migrations.RemoveField(
            model_name="alexandriauser",
            name="is_manager",
        ),
        migrations.AddField(
            model_name="alexandriauser",
            name="notes",
            field=models.TextField(blank=True, null=True, verbose_name="notes"),
        ),
    ]