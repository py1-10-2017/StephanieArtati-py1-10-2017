from django import template

register = template.Library()

@register.filter(name='times')
def times(number):
    return range(number)

@register.filter(name='deltatofive')
def deltatofive(number):
    remaining = 5-number
    return range(remaining)
