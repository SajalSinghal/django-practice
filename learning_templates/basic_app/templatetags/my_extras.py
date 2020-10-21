from django import template

register = template.Library()

@register.filter(name='cutWord')    #using decorator
def cutWord(value, arg):
    '''
    This cuts out all the values of "arg" from the string
    '''

    return value.replace(arg, '')

# register.filter('cut', cut)  as cut is already a built-in filter
