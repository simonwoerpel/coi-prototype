import re

from django import template

register = template.Library()


@register.filter
def hilight(text, val):
    tag = '<span class="hilight">{}</span>'.format(val.title())
    pattern = re.compile(val, re.IGNORECASE)
    return pattern.sub(tag, text)
