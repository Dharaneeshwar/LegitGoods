# Generated by Django 3.1.2 on 2020-11-05 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_user_payout'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestPayout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=50)),
                ('amount', models.IntegerField(default=0)),
            ],
        ),
    ]
