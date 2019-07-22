# Generated by Django 2.1.7 on 2019-07-21 13:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190720_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='height',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(250)]),
        ),
    ]
