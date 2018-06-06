import markdown
import re
from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter('markdown', needs_autoescape=True)
def markdown_filter(text, autoescape=True):
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    return mark_safe(markdown.markdown(esc(text)))

@register.filter()
def absolute_url(value):
    if not value:
        return ''
    if re.match(r'^(?:http|\/\/)', value):
        return value
    return '//' + value

@register.inclusion_tag('django_presskit/navitem.html')
def optional_navitem(item, anchor, title):
    return {
        'item': item,
        'anchor': anchor,
        'title': title
    }
