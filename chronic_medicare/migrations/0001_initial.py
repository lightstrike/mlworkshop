# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChronicConditionLinearRegression',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('parameters', models.CharField(max_length=512)),
                ('coefficient', models.FloatField(max_length=64)),
                ('constant', models.FloatField(default=0, max_length=64)),
                ('p_value', models.FloatField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='MedicareFile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('csv_file', models.FileField(upload_to='medicare-files/')),
            ],
        ),
    ]
