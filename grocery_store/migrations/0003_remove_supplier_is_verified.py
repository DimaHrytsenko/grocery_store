# Generated by Django 4.1.3 on 2022-11-14 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_store', '0002_supplier_is_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='is_verified',
        ),
    ]
