# Generated by Django 4.0.2 on 2022-04-27 06:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_forms', '0003_alter_ovchivmanagement_substitution_firstline_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ovchivmanagement',
            name='substitution_firstline_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 27, 9, 28, 23, 648142)),
        ),
    ]