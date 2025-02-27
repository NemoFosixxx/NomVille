from django import template

register = template.Library()

@register.filter
def replace_pipe_with_newline(value):
    """Заменяет символы '|' на новую строку."""
    if isinstance(value, str):
        return value.replace('|', '\n')
    return value
