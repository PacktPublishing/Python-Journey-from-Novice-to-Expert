# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(unique=True, max_length=64)),
                ('username', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('url', models.URLField(max_length=255, null=True, blank=True)),
                ('password', models.CharField(max_length=2048)),
                ('notes', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
