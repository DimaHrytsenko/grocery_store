# Generated by Django 4.1.3 on 2022-11-25 09:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_store', '0012_feedback_written_by_alter_feedback_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='created',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2022, 11, 25, 11, 35, 15, 946979)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='created',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2022, 11, 25, 11, 35, 15, 945979)),
        ),
    ]
