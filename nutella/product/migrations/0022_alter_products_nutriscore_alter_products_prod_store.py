# Generated by Django 4.1.3 on 2022-12-16 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0021_categories_products_remove_product_categories_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="nutriscore",
            field=models.TextField(max_length=1),
        ),
        migrations.AlterField(
            model_name="products",
            name="prod_store",
            field=models.TextField(max_length=1500, null=True),
        ),
    ]
