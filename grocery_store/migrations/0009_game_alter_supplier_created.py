# Generated by Django 4.1.3 on 2022-11-19 19:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_store', '0008_alter_supplier_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='PING', max_length=4)),
                ('computer', models.CharField(default='PONG', max_length=4)),
            ],
            options={
                'verbose_name': 'Game',
                'verbose_name_plural': 'Games',
            },
        ),
        migrations.AlterField(
            model_name='supplier',
            name='created',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2022, 11, 19, 21, 5, 25, 927005)),
        ),
    ]
