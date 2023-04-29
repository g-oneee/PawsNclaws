# Generated by Django 4.0.3 on 2022-11-25 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_adopt_is_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adopt',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='adopt/ecomerce/adopt_img'),
        ),
        migrations.AlterField(
            model_name='adopt',
            name='is_available',
            field=models.CharField(default='yes', max_length=100),
        ),
    ]
