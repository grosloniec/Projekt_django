# Generated by Django 5.0.6 on 2024-05-26 19:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "reservations",
            "0005_alter_samochod_options_samochod_make_samochod_model_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="samochod",
            name="make",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AlterField(
            model_name="samochod",
            name="model",
            field=models.CharField(default="", max_length=255),
        ),
    ]
