# Generated by Django 4.1.3 on 2022-12-16 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0023_alter_products_nutriscore_alter_products_prod_store"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="first_name",
            field=models.TextField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="second_name",
            field=models.TextField(blank=True, max_length=254),
        ),
    ]
