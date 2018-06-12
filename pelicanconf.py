#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'esc'
SITENAME = u'Eflatun Siber Guvenlik'
SITEURL = 'https://eflatunakademi.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Istanbul'

DEFAULT_LANG = u'tr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter','https://twitter.com/ozdmrhh'), 
	('Linkedin', 'https://www.linkedin.com/in/huriye-%C3%B6zdemir-2a3435116/'),
	('Instagram', 'https://github.com/huriozdmr'),
	('Youtube', 'https://github.com/huriozdmr'))

DEFAULT_PAGINATION = 10
THEME = "themes/marble"

USE_FOLDER_AS_CATEGORY = True
DISPLAY_CATEGORIES_ON_MENU = True
SUMMARY_MAX_LENGTH = None

ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'

DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives']
PAGINATED_DIRECT_TEMPLATES = ['index']
NEWEST_FIRST_ARCHIVES = True


PLUGIN_PATHS = ['pelican-plugins', ]
PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
