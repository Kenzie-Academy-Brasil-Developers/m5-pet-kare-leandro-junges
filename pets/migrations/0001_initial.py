# Generated by Django 4.1.3 on 2022-12-01 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("groups", "0001_initial"),
        ("traits", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Pet",
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
                ("age", models.IntegerField()),
                ("weight", models.FloatField()),
                (
                    "sex",
                    models.CharField(
                        choices=[
                            ("Male", "Male"),
                            ("Female", "Female"),
                            ("Not Informed", "Default"),
                        ],
                        default="Not Informed",
                        max_length=20,
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="groups",
                        to="groups.group",
                    ),
                ),
                (
                    "trait",
                    models.ManyToManyField(related_name="trait", to="traits.trait"),
                ),
            ],
        ),
    ]