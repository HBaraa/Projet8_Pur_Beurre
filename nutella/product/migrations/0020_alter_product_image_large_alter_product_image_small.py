# Generated by Django 4.1.3 on 2022-12-07 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0019_remove_product_image_product_image_large_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image_large",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="image_small",
            field=models.TextField(null=True),
        ),
    ]
