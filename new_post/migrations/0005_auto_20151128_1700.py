# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_post', '0004_remove_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='post',
            name='submitter',
            field=models.TextField(default=b''),
        ),
    ]
