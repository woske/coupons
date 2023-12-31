# Generated by Django 4.2.3 on 2023-10-04 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0028_store_index_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='index_page',
            field=models.BooleanField(default=True, help_text='Check this to allow indexing of the page.'),
        ),
        migrations.AddField(
            model_name='couponindexpage',
            name='index_page',
            field=models.BooleanField(default=True, help_text='Check this to allow indexing of the page.'),
        ),
        migrations.AddField(
            model_name='storeindexpage',
            name='index_page',
            field=models.BooleanField(default=True, help_text='Check this to allow indexing of the page.'),
        ),
    ]
