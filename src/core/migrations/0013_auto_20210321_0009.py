# Generated by Django 3.1.6 on 2021-03-20 15:09

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_billingaddress_apartment_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingaddress',
            name='countries',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]