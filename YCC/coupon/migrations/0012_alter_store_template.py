# Generated by Django 4.2.3 on 2023-09-28 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0011_alter_store_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='template',
            field=models.CharField(choices=[('store/store_index_page.html', 'Template Box'), ('store/store_index_page_lines.html', 'Template Lines')], default='store/store_index_page.html', max_length=255),
        ),
    ]
