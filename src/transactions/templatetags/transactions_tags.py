from django import template
import locale
locale.setlocale(locale.LC_ALL, '')

register = template.Library()
 
@register.filter()
def currency(value):
    if value < 0:
        val = float(str(value)[1:])
        return "-" + locale.currency(val, grouping=True)            
    return locale.currency(value, grouping=True)