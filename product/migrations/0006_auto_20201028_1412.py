# Generated by Django 3.1.2 on 2020-10-28 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20201028_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image2',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='media'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image3',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='media'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='default.jpg', upload_to='media'),
        ),
    ]
