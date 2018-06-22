#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
SITENAME = 'Eflatun Siber Güvenlik'
SITETITLE = u'Eflatun Siber Güvenlik'
AUTHOR = u'esc'
SITEURL = 'https://eflatunakademi.github.io'
SITEDESCRIPTION = "Eflatun Siber Güvenlik"
PATH = 'content'
SITESUBTITLE = 'Siber Dünyaya Adım Atın!'
PYGMENTS_STYLE = 'monokai'
SITELOGO = '/images/logo.png'
TIMEZONE = 'Europe/Istanbul'

DEFAULT_LANG = u'tr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None



# Social widget
SOCIAL = (('twitter','https://twitter.com/EflatunAkademi'), 
	('linkedin', 'https://tr.linkedin.com/company/eflatun-akademi'),
	('instagram', 'https://www.instagram.com/eflatunakademi/?hl=tr'),
	('youtube', 'https://www.youtube.com/channel/UC924GxT83BxD-aii5fCuyig'))

DEFAULT_PAGINATION = 10
THEME = "themes/Flex"

MAIN_MENU = True
HOME_HIDE_TAGS = True
USE_FOLDER_AS_CATEGORY = True
DISPLAY_CATEGORIES_ON_MENU = False
SUMMARY_MAX_LENGTH = 20
MENUITEMS = False


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
