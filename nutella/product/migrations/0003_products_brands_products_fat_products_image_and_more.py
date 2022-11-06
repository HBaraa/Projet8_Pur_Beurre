# Generated by Django 4.1.3 on 2022-11-06 12:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_remove_products_brands_remove_products_fat_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="products",
            name="brands",
            field=models.CharField(
                default=django.utils.timezone.now,
                max_length=100,
                verbose_name="Marques du produit",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="products",
            name="fat",
            field=models.FloatField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="products",
            name="image",
            field=models.URLField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="products",
            name="link",
            field=models.URLField(default="", unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="products",
            name="salt",
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="products",
            name="saturated_fat",
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="products",
            name="sugars",
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
