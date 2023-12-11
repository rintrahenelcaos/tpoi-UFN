# Generated by Django 4.2.7 on 2023-12-11 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Libro",
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
                ("titulo", models.CharField(max_length=100)),
                ("autor", models.CharField(max_length=100)),
                ("temas", models.CharField(max_length=100)),
                ("dispon", models.BooleanField()),
            ],
        ),
    ]
