# Generated by Django 4.2.2 on 2023-12-08 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("elibrary_app", "0003_delete_login_delete_register"),
    ]

    operations = [
        migrations.AddField(
            model_name="ebooksmodel",
            name="author_id",
            field=models.IntegerField(default=0),
        ),
    ]
