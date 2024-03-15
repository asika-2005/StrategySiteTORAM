from django import template

register = template.Library()


@register.simple_tag
def url_replace(request, faild, value):
  url_dict = request.GET.copy()
  url_dict[faild] = str(value)

  return url_dict.urlencode()