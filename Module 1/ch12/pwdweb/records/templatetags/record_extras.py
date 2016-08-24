# -*- coding: utf-8 -*-
from django import template
from django.utils.html import escape


register = template.Library()


@register.simple_tag
def hide_password(password):
    return '<span title="{0}">{1}</span>'.format(
        escape(password), '*' * len(password))
