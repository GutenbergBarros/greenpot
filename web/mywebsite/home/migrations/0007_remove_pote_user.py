# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20160928_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pote',
            name='user',
        ),
    ]
