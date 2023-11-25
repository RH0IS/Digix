# Generated by Django 4.2.7 on 2023-11-25 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("coinmarketapp", "0003_trending_crypto"),
    ]

    operations = [
        migrations.AddField(
            model_name="trending_crypto",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]
