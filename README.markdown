# OpenGraph App for Django >= 1.4

Adds HTML Meta tags for OpenGraph support.

* [OpenGraph](https://dev.twitter.com/docs/cards)
* [Facebook OpenGraph](http://davidwalsh.name/twitter-cards)
    
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
    'SITE_NAME': 'Your Site Name',
    'DEFAULT_IMAGE': '%sdefault/image.png' % STATIC_URL
}
```

* `FB_ADMINS`: __optional__
  Something here

* `FB_APP_ID`: __optional__
  Something here

* `SITE_NAME`:
  Name of your site
  
* `DEFAULT_IMAGE`: __optional__
  Default image to use in the open graph.

### Loading Template Tags

1. Load the `twittercard` custom tags
2. Call the `twittercard_summary` or `twittercard_photo` tag, passing in the appropriate parameters

```html
{% load twittercard %}
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Django TwitterCard Example</title>
        {% twittercard_summary title="Foo" description="Bar" %}
    </head>
    <body></body>
</html>
```

The result, including the use of the TWITTERCARD_CONFIG options defined above, would be:

```html
<meta name="twitter:card" content="summary">
<meta name="twitter:site" content="@foo">
<meta name="twitter:site:id" content="foo">
<meta name="twitter:creator" content="@bar">
<meta name="twitter:creator:id" content="bar">
<meta name="twitter:url" content="http://url.tld/sub/">
<meta name="twitter:title" content="Foo"/>
<meta name="twitter:description" content="Bar">
```

## Summary TwitterCard

The [summary card](https://dev.twitter.com/docs/cards#summary-card) can be used for many kinds of web content, from blog posts and news articles, to products and restaurants.

```
{% twittercard_summary site="" site_id="" creator="" creator_id="" url="" title="" description="" image="" %}
```

* `site`: __optional__  
  @username for the website used in the card footer.  Will default to TWITTERCARD_CONFIG if supplied.

* `site_id`: __optional__  
  Same as site, but the website's Twitter user ID instead. Note that user ids never change, while @usernames can be changed by the user.  Will default to TWITTERCARD_CONFIG if supplied.

* `creator`: __optional__  
  @username for the content creator / author.

* `creator_id`: __optional__  
  Same as twitter:creator, but the Twitter user's ID.

* `url`: __required if not in OpenGraph__  
  Will fallback to *OpenGraph url* if available.  Will default to the current page URL.  Canonical URL of the card content.

* `title`: __required if not in OpenGraph__  
  Will fallback to *OpenGraph title* if available. Title should be concise and will be truncated at 70 characters.

* `description`: __required if not in OpenGraph__  
  Will fallback to *OpenGraph description* if available.  A description that concisely summarizes the content of the page, as appropriate for presentation within a Tweet. Do not re-use the title text as the description, or use this field to describe the general services provided by the website. Description text will be truncated at the word to 200 characters.

* `image`: __optional__  
  Will fallback to *OpenGraph image* if available.  URL to a unique image representing the content of the page. Do not use a generic image such as your website logo, author photo, or other image that spans multiple pages. Images larger than 120x120px will be resized and cropped square based on longest dimension. Images smaller than 60x60px will not be shown.  

## Photo TwitterCard

The [photo card](https://dev.twitter.com/docs/cards#photo-card) puts the image front and center in the Tweet.

```
{% twittercard_photo site="" site_id="" creator="" creator_id="" title="" description="" image="" image_width="" image_height="" %}
```

* `site`: __optional__  
  @username for the website used in the card footer.  Will default to TWITTERCARD_CONFIG if supplied.

* `site_id`: __optional__  
  Same as site, but the website's Twitter user ID instead. Note that user ids never change, while @usernames can be changed by the user.  Will default to TWITTERCARD_CONFIG if supplied.

* `creator`: __optional__  
  @username for the content creator / author.

* `creator_id`: __optional__  
  Same as twitter:creator, but the Twitter user's ID.

* `title`: __optional__  
  Will fallback to *OpenGraph title* if available.  See full explanation of title in the Summary Card.

* `description`: __optional__  
  Will fallback to *OpenGraph description* if available.  See full explanation of description in the Summary Card.

* `image`: __required if not in OpenGraph__  
  Will fallback to *OpenGraph image* if available.  A URL to the image representing the content.

* `image_width`: __optional__  
  Will fallback to *OpenGraph image width* if available.  Providing width in px helps us more accurately preserve the the aspect ratio of the image when resizing.

* `image_height`: __optional__  
  Will fallback to *OpenGraph image height* if available.  Providing height in px helps us more accurately preserve the the aspect ratio of the image when resizing.

## Player TwitterCard

**Currently not supported in django-twittercard**.  The [player card](https://dev.twitter.com/docs/cards#player-card) is for interactive media experiences like videos, music players, and live streaming events.

**NOTE**: If any required fields are omitted, the card may not be shown in the Tweet.

## TODO

* [Check for required fields based on card type](https://github.com/leveille/django-twittercard/issues/1)
* [Add support for player card](https://github.com/leveille/django-twittercard/issues/2)

