from django import template

register = template.Library()

@register.filter
def newline_to_pipe(value):
    if isinstance(value, str):
        return value.replace('\n', '|')
    return value
