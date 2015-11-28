# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='downvote',
        ),
        migrations.RemoveField(
            model_name='post',
            name='upvote',
        ),
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
        migrations.AddField(
            model_name='post',
            name='up_vote',
            field=models.IntegerField(default=0),
        ),
    ]
