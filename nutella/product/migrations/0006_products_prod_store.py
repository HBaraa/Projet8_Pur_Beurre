# Generated by Django 4.1.3 on 2022-11-06 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0005_products_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="products",
            name="prod_store",
            field=models.CharField(default="", max_length=150),
            preserve_default=False,
        ),
    ]
