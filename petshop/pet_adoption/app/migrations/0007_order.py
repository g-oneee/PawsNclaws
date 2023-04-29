# Generated by Django 4.0.3 on 2022-10-09 15:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0006_adopt_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ecomerce/order/image')),
                ('product', models.CharField(default='', max_length=1000)),
                ('quantity', models.CharField(max_length=10)),
                ('price', models.IntegerField()),
                ('total', models.CharField(default='', max_length=100)),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=10)),
                ('pincode', models.CharField(max_length=6)),
                ('address', models.TextField()),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]