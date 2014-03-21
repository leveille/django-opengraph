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
    request = context['request']
    graph = {'title': kwargs.get('title', None), 'description': kwargs.get('description', None),
             'type': kwargs.get('type', 'website'), 'url': kwargs.get('url', request.build_absolute_uri())}

    config = getattr(settings, 'OPENGRAPH_CONFIG', {})
    graph['fb_admins'] = kwargs.get('fb_admins', config.get('FB_ADMINS', None))
    graph['fb_app_id'] = kwargs.get('fb_app_id', config.get('FB_APP_ID', None))
    graph['site_name'] = kwargs.get('site_name', config.get('SITE_NAME', None))
    default_image = normalize_image_url(request, config.get('DEFAULT_IMAGE', None))

    images = []
    if default_image is not None:
        images.append(default_image)
    image = kwargs.get('image', None)
    if isinstance(image, types.ListType):
        images = [normalize_image_url(request, img) for img in image]
        images.insert(0, default_image)
    elif isinstance(image, types.StringType) or isinstance(image, SafeUnicode) or isinstance(image, unicode):
        images = [normalize_image_url(request, image)]
    graph['images'] = images
    return graph


def normalize_image_url(request, image):
    if image is None or image[:4] == 'http':
        return image
    protocol = 'http'
    if request.is_secure():
        protocol = 'https'
    if image[:2] == '//':
        return '%s:%s' % (protocol, image)
    host = request.get_host()
    return '%s://%s%s' % (protocol, host, image)
