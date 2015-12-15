# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist_tracker', '0003_invite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invite',
            name='recipient',
            field=models.EmailField(max_length=254),
        ),
    ]
