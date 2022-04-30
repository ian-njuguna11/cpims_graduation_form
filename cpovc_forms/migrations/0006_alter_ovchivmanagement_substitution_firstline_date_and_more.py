# Generated by Django 4.0.2 on 2022-04-30 08:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_forms', '0005_ovcprevsinovyoteenevaluation_event_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ovchivmanagement',
            name='substitution_firstline_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 30, 11, 16, 5, 466135)),
        ),
        migrations.AlterField(
            model_name='ovcprevsinovyoteenevaluation',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_forms.ovcpreventiveevents'),
        ),
    ]
