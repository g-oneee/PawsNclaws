# Generated by Django 4.0.3 on 2022-10-31 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_contact_us_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='adopt',
            name='vaccineinfo',
            field=models.CharField(default='DHPP', max_length=100),
        ),
    ]
