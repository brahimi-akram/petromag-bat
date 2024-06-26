from django import template
from datetime import timedelta

register = template.Library()

@register.filter
def add_days(value, days):
    """
    Adds the specified number of days to the given date.
    """
    return value + timedelta(days=days)
