# Generated by Django 4.1.2 on 2022-10-18 13:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 10, 18, 15, 14, 3, 75685)),
        ),
    ]
