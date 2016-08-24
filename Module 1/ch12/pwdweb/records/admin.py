# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Record


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'username', 'email', 'url', 'created',
        'last_modified', 'password'
    )
