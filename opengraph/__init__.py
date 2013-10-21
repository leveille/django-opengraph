__all__ = ('VERSION',)

try:
    VERSION = __import__('pkg_resources') \
        .get_distribution('django-opengraph').version
except Exception, e:
    VERSION = 'unknown'
