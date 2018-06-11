# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import sys
sys.path.append('.')


AUTHOR = u'Esc'
SITENAME = u'Eflatun Siber Güvenlik'
SITEURL = 'https://eflatunakademi.github.io'

TIMEZONE = 'Europe/Istanbul'

from utils import filters
JINJA_FILTERS = { 'foo': filters.printfoo, 'sidebar': filters.sidebar }

DEFAULT_LANG = u'tr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter','https://twitter.com/ozdmrhh'), 
	('Linkedin', 'https://www.linkedin.com/in/huriye-%C3%B6zdemir-2a3435116/'),
	('Instagram', 'https://github.com/huriozdmr')
	('Youtube', 'https://github.com/huriozdmr'))

DEFAULT_PAGINATION = 10
POST_LIMIT = 3

RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = True

# Formatting for dates
DEFAULT_DATE_FORMAT = ('%a %d %B %Y')


# Formatting for urls
# ARTICLE_DIR = 'blog'
ARTICLE_URL = "blog/{slug}"
ARTICLE_SAVE_AS = "blog/{slug}/index.html"

ARCHIVES_URL = "blog"
ARCHIVES_SAVE_AS = "blog/index.html"

PAGE_DIR = 'pages'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

USE_FOLDER_AS_CATEGORY = True

# Generate yearly archive
YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'

# Show most recent posts first
NEWEST_FIRST_ARCHIVES = True


THEME = "themes/twenty"

STATIC_PATHS = ['images',
                'fonts',
                'css',
                'js',
                ]
