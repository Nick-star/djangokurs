from django import template

register = template.Library()


@register.filter
def round_value(value):
    return round(value)

@register.filter
def to_int(value):
    return int(value)