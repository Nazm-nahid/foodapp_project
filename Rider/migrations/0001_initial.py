# Generated by Django 3.0.8 on 2020-07-28 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resturent', models.CharField(max_length=200)),
                ('deli_address', models.CharField(max_length=400)),
                ('time', models.TimeField()),
                ('rider_ac', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resturent', models.CharField(max_length=200)),
                ('order_item', models.CharField(max_length=50)),
                ('time', models.TimeField()),
                ('payment', models.CharField(max_length=3)),
                ('rider_ac', models.CharField(max_length=200)),
            ],
        ),
    ]