from django.template import Library

register = Library()

@register.filter
def my_uppercase(my_str):
    return str(my_str).upper()

