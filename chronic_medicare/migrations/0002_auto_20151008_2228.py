# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chronic_medicare', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chronicconditionlinearregression',
            old_name='p_value',
            new_name='r_squared',
        ),
    ]
