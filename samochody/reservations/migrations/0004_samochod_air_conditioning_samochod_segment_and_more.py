# Generated by Django 5.0.6 on 2024-05-26 19:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reservations", "0003_samochod_luggage_capacity_alter_samochod_fuel_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="samochod",
            name="air_conditioning",
            field=models.CharField(
                choices=[("AUTOMATIC", "automatic"), ("MANUAL", "manual")],
                default="MANUAL",
                max_length=16,
            ),
        ),
        migrations.AddField(
            model_name="samochod",
            name="segment",
            field=models.CharField(
                choices=[("AUTOMATIC", "automatic"), ("MANUAL", "manual")],
                default="A",
                max_length=16,
            ),
        ),
        migrations.AlterField(
            model_name="samochod",
            name="body_type",
            field=models.CharField(
                choices=[
                    ("SEDAN", "sedan"),
                    ("WAGON", "wagon"),
                    ("HATCHBACK", "hatchback"),
                    ("CONVERTIBLES", "convertibles"),
                    ("SUV", "SUV"),
                    ("VAN", "van"),
                ],
                max_length=16,
            ),
        ),
    ]
