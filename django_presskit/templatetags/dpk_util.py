import markdown
import re
from urlparse import urlparse
from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter('markdown')
def markdown_filter(text):
    return mark_safe(markdown.markdown(text))

@register.filter()
def with_protocol(value):
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

@register.filter()
def domain(value):
    if not value:
        return ''
    if re.match(r'^(?:http|\/\/)', value):
        return urlparse(value).netloc
    return urlparse('//' + value).netloc

@register.simple_tag(takes_context=True)
def absolute_url(context, viewname, *args, **kwargs):
    # Some code cribbed from Django's `url` tag.
    from django.urls import reverse, NoReverseMatch

    url = reverse(viewname, args=args, kwargs=kwargs)
    return context.request.build_absolute_uri(url)

@register.tag
def condense(parser, token):
    nodelist = parser.parse(('endcondense',))
    parser.delete_first_token()
    return CondenseNode(nodelist)

class CondenseNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
    def render(self, context):
        output = self.nodelist.render(context)
        return re.sub(r'\s*\n+', '\n', output)
