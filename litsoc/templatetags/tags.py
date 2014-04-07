from django import template

register = template.Library()

@register.simple_tag
def path_compare(request, pattern):
    path = request
    print pattern
    print path
    if pattern in path:
        print 'Yes'
        return 'active'
    print 'No'
    return ''