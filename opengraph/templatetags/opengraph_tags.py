import types
from django import template
from django.conf import settings
from django.db.models.query import QuerySet
from django.utils.safestring import SafeUnicode
register = template.Library()


@register.inclusion_tag('opengraph/base.html', takes_context=True)
def opengraph(context, *args, **kwargs):
    graph = get_opengraph_attributes(context, kwargs)
    return graph


def get_opengraph_attributes(context, kwargs):
    graph = {}
    graph['title'] = kwargs.get('title', None)
    graph['description'] = kwargs.get('description', None)
    graph['type'] = kwargs.get('type', 'site')
    request = context['request']
    graph['url'] = kwargs.get('url', request.build_absolute_uri())

    image = kwargs.get('image', None)
    default_image = None

    config = getattr(settings, 'OPENGRAPH_CONFIG', None)
    if config is not None:
        graph['fb_admins'] = kwargs.get('fb_admins', config.get('FB_ADMINS', None))
        graph['fb_app_id'] = kwargs.get('fb_app_id', config.get('FB_APP_ID', None))
        graph['site_name'] = kwargs.get('site_name', config.get('SITE_NAME', None))
        default_image = config.get('DEFAULT_IMAGE', None)

    if default_image is not None and 'http' not in default_image:
        default_image = '%s%s' % (request.build_absolute_uri(), default_image)

    images = [default_image]
    if isinstance(image, types.ListType):
        images = image
        images.insert(0, default_image)
    elif isinstance(image, QuerySet):
        images = [img.image for img in image]
        images.insert(0, default_image)
    elif isinstance(image, types.StringType) or isinstance(image, SafeUnicode) or isinstance(image, unicode):
        if image is not None and 'http' not in image:
            image = '%s%s' % (request.build_absolute_uri(), image)
        images = [image]
    if images:
        graph['images'] = images
    return graph
