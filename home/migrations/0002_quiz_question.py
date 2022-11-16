# Generated by Django 4.1.3 on 2022-11-16 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="quiz_question",
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
                ("question_id", models.IntegerField()),
                ("question", models.TextField()),
                ("option_1", models.TextField()),
                ("option_2", models.TextField()),
                ("option_3", models.TextField()),
                ("option_4", models.TextField()),
                ("answer", models.TextField()),
            ],
        ),
    ]