# Generated by Django 4.2.3 on 2023-08-29 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_product_buyer_id_product_selled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='buyer_id',
            field=models.IntegerField(null=True),
        ),
    ]
