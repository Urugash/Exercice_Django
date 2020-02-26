from django import template
register = template.Library()

from ..models import Article

@register.simple_tag
def any_function():
    return Article.objects.count()
