# Generated by Django 4.2.3 on 2023-08-16 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='user_id',
            field=models.IntegerField(default=1),
        ),
    ]