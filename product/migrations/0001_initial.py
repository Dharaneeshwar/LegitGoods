# Generated by Django 3.1.2 on 2020-10-27 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('subtitle', models.CharField(max_length=50)),
                ('stars', models.FloatField(default=0.0)),
                ('num_rating', models.IntegerField(default=0)),
                ('marked_price', models.FloatField()),
                ('selling_price', models.FloatField()),
                ('product_image', models.ImageField(upload_to='')),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('offer_present', models.BooleanField(default=False)),
                ('userid', models.CharField(max_length=50)),
                ('tags', models.ManyToManyField(to='product.Tag')),
            ],
        ),
    ]
