# Generated by Django 4.2.2 on 2023-06-17 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0005_coupon_external_link_store_external_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='external_link',
            field=models.URLField(),
        ),
    ]
