# Generated by Django 4.2.1 on 2023-05-22 08:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_product_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(default='', upload_to='uploads/'),
            preserve_default=False,
        ),
    ]