# OpenGraph App for Django >= 1.4

Adds HTML Meta tags for OpenGraph support.

* [OpenGraph](http://ogp.me/)
* [Facebook OpenGraph](https://developers.facebook.com/docs/opengraph/property-types/)
    
## Installation

```
pip install -e git+git://github.com/leveille/django-opengraph.git#egg=opengraph
```

## Upgrade

```
pip install -U -e git+git://github.com/leveille/django-opengraph.git#egg=opengraph
```

## Usage

### Optional Configuration

1. Add opengraph to your settings.py INSTALLED_APPS list
2. There are a few configuration options to opengraph that can be placed in an OPTIONAL dictionary called OPENGRAPH_CONFIG in settings.py.

```python
OPENGRAPH_CONFIG = {
    'FB_ADMINS': '###',
    'FB_APP_ID': '###',
    'DEFAULT_IMAGE': '%sdefault/image.png' % STATIC_URL,
    'SITE_NAME': 'Your Site Name',
}
```

* `FB_ADMINS`: __optional__
  Something here

* `FB_APP_ID`: __optional__
  Something here

* `DEFAULT_IMAGE`: __optional__
  Default image to use in the open graph.

* `SITE_NAME`:
  Name of your site

### Loading Template Tags

1. Load the `opengraph_tags` custom tags
2. Call the `opengraph` tag, passing in the appropriate parameters

Assume the following configuration:

```python
OPENGRAPH_CONFIG = {
    'FB_ADMINS': '123',
    'FB_APP_ID': '456',
    'DEFAULT_IMAGE': '%sdefault/image.png' % STATIC_URL,
    'SITE_NAME': 'Your Site Name',
}
```

```html
{% load opengraph_tags %}
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Django OpenGraph Example</title>
        {% opengraph title='Django OpenGraph Example' description='This is a test' image="http://site.tld/image.png" %}
    </head>
    <body></body>
</html>
```

The result, including the use of the OPENGRAPH_CONFIG options defined above, would be:

```html
<meta property="fb:admins" content="123">
<meta property="fb:app_id" content="456">
<meta property="og:title" content="Django OpenGraph Example">
<meta property="og:type" content="website">
<meta property="og:url" content="http://127.0.0.1:8000/">
<meta property="og:image" content="http://site.tld/image.png">
<meta property="og:description" content="This is a test">
<meta property="og:site_name" content="Your Site Name">
```

## OpenGraph Tag

```
{% opengraph fb_admins="" fb_app_id="" site_name="" type="" url="" title="" description="" image="" %}
```

* `fb_admins`: __optional__
  The ID (or comma-separated list for properties that can accept multiple IDs) of an app, person using the app, or Page Graph API object.

* `fb_app_id`: __optional__
  The ID of your Facebook Application

* `site_name`: __required if not defined by `SITE_NAME` in `OPENGRAPH_CONFIG` __
  If your object is part of a larger web site, the name which should be displayed for the overall site. e.g., "IMDb"

* `type`: __optional__
  The type of your object, e.g., "video.movie".
  Defaults to `website`

* `url`: _optional_
  The canonical URL of your object that will be used as its permanent ID in the graph, e.g., "http://www.imdb.com/title/tt0117500/".
  Defaults to `request.build_absolute_url()`

* `title`: __required__
  The title of your object as it should appear within the graph, e.g., "The Rock".  Title should be concise as it may be truncated depending on where it is used (in the NewsFeed, etc).

* `description`: __optional__
  A one to two sentence description of your object.  Description should be concise as it may be truncated depending on where it is used (in the NewsFeed, etc).

* `image`: __required if not defined by `DEFAULT_IMAGE` in `OPENGRAPH_CONFIG` __
  An image URL which should represent your object within the graph.
  Defaults to `DEFAULT_IMAGE` if defined in `OPENGRAPH_CONFIG`

