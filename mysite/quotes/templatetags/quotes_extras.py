from django import template
register = template.Library()

def wikipedia_url(value):
    dict = {'-':'_','.':'._',' ':'_'}
    value=value.title()
    for target,replacement in dict.items():
        value = value.replace(target,replacement)
    return value

register.filter('wikipedia_url', wikipedia_url)
