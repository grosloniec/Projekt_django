# Generated by Django 5.0.6 on 2024-05-30 17:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reservations", "0007_klient"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="klient",
            options={"verbose_name": "Klient", "verbose_name_plural": "Klienci"},
        ),
        migrations.AddField(
            model_name="klient",
            name="driving_license_since",
            field=models.DateField(default=datetime.date(1900, 1, 1)),
        ),
        migrations.AlterField(
            model_name="klient",
            name="birthday",
            field=models.DateField(),
        ),
    ]
