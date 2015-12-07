# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist_tracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('artist_name', models.CharField(max_length=120, null=True, blank=True)),
                ('genre', models.CharField(max_length=64, null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=200, null=True, blank=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('concert_name', models.CharField(max_length=120, null=True, blank=True)),
                ('venue', models.CharField(max_length=120, null=True, blank=True)),
                ('city', models.CharField(max_length=120, null=True, blank=True)),
                ('state', models.CharField(max_length=120, null=True, blank=True)),
                ('country', models.CharField(max_length=120, null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConcertOf',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateField()),
                ('artist', models.ForeignKey(to='artist_tracker.Artist')),
                ('concert', models.ForeignKey(to='artist_tracker.Concert')),
            ],
        ),
        migrations.AddField(
            model_name='artist',
            name='concerts',
            field=models.ManyToManyField(to='artist_tracker.Concert', through='artist_tracker.ConcertOf'),
        ),
    ]
