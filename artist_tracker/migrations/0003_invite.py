# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artist_tracker', '0002_auto_20151207_0144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=120, null=True, blank=True)),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
                ('artist', models.ForeignKey(to='artist_tracker.Artist')),
                ('concert', models.ForeignKey(to='artist_tracker.Concert')),
                ('recipient', models.ForeignKey(related_name='invite_recipient', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(related_name='invite_sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
