# Generated by Django 4.2.1 on 2023-05-30 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Medicine",
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
                ("name", models.CharField(max_length=255)),
                ("weight", models.IntegerField(default=0)),
                ("code", models.CharField(max_length=255)),
                ("image", models.ImageField(upload_to="medication/")),
            ],
            options={
                "verbose_name": "Medicine",
                "verbose_name_plural": "Medicines",
                "db_table": "medicines",
            },
        ),
    ]
