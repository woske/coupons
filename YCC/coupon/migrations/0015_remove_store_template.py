# Generated by Django 4.2.3 on 2023-09-28 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0014_alter_store_template'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='template',
        ),
    ]
