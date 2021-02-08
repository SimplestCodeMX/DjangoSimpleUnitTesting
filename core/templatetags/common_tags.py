from django.utils.html import mark_safe
from django import template
register = template.Library()


@register.simple_tag
def relative_url(value, field_name, urlencode=None, exclude=None):
    url = f'?{field_name}={value}'

    if urlencode:
        querystring = urlencode.split('&')
        filtered_querystring = filter(
            lambda p: p.split('=')[0] != field_name and field_name not in [exclude],
            querystring
        )
        params_list = list(filtered_querystring)
        encoded_querystring = '&'.join(params_list)
        url = f'{url}&{encoded_querystring}'
    return url
