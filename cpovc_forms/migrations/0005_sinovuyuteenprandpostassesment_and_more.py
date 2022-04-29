# Generated by Django 4.0.2 on 2022-04-28 17:12

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_registry', '0001_initial'),
        ('cpovc_ovc', '0001_initial'),
        ('cpovc_forms', '0004_alter_ovchivmanagement_substitution_firstline_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='SinovuyuTeenPrAndPostAssesment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assment_type', models.IntegerField(default=0)),
                ('date_assment', models.CharField(max_length=256)),
            ],
        ),
        migrations.AlterField(
            model_name='ovchivmanagement',
            name='substitution_firstline_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 28, 20, 12, 6, 55429)),
        ),
        migrations.CreateModel(
            name='NewGraduationMonitoring',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_id', models.IntegerField(max_length=3)),
                ('bench_mark_1', models.IntegerField(default=0)),
                ('bench_mark_2', models.IntegerField(default=0)),
                ('bench_mark_3', models.IntegerField(default=0)),
                ('bench_mark_4', models.IntegerField(default=0)),
                ('bench_mark_5', models.IntegerField(default=0)),
                ('bench_mark_6', models.IntegerField(default=0)),
                ('bench_mark_7', models.IntegerField(default=0)),
                ('bench_mark_8', models.IntegerField(default=0)),
                ('bench_mark_9', models.IntegerField(default=0)),
                ('date_of_event', models.DateField(default=django.utils.timezone.now)),
                ('timestamp_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('timestamp_updated', models.DateTimeField(auto_now=True)),
                ('care_giver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regperson')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_forms.ovccareevents')),
                ('household', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_ovc.ovchousehold')),
            ],
            options={
                'db_table': 'new_graduation_monitoring',
            },
        ),
    ]
