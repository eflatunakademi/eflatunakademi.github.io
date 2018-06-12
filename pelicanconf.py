#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'esc'
SITENAME = u'Eflatun Siber Guvenlik'
SITEURL = 'https://eflatunakademi.github.io'
SITEDESCRIPTION = "Eflatun Siber Güvenlik"
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
SOCIAL = (('Twitter','https://twitter.com/EflatunAkademi'), 
	('Linkedin', 'https://tr.linkedin.com/company/eflatun-akademi'),
	('Instagram', 'https://www.instagram.com/eflatunakademi/?hl=tr'),
	('Youtube', 'https://www.youtube.com/channel/UC924GxT83BxD-aii5fCuyig'))

DEFAULT_PAGINATION = 10
THEME = "marble"

USE_FOLDER_AS_CATEGORY = True
DISPLAY_CATEGORIES_ON_MENU = True
SUMMARY_MAX_LENGTH = None

ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'

DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives']
PAGINATED_DIRECT_TEMPLATES = ['index']
NEWEST_FIRST_ARCHIVES = True

LOGO = "/images/index.jpeg"
PLUGIN_PATHS = ['pelican-plugins', ]
PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
