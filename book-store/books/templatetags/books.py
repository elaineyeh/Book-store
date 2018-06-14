from django import template
from django.urls import reverse

from urllib.parse import urlencode


register = template.Library()


@register.filter(name='build_links')
def build_links(obj_list, field_name):
    base_url = reverse('books:index')
    links = []
    for o in obj_list:
        params = urlencode({field_name: o.id})
        url = '{}?{}'.format(base_url, params)
        tag = '<a href="{}">{}</a>'.format(url, o.name)
        links.append(tag)

    return links
