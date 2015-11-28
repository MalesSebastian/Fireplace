# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_post', '0002_auto_20151128_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='submitter',
        ),
    ]
