# Generated by Django 4.1.2 on 2023-02-18 14:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 2, 18, 16, 17, 35, 475155)),
        ),
    ]
