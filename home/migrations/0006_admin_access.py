# Generated by Django 4.1.3 on 2022-11-17 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_quiz_question_option_1_image_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="admin_access",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("control", models.CharField(max_length=255)),
                ("value", models.BooleanField()),
            ],
        ),
    ]