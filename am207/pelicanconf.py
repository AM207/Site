#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Pavlos Protopapas'
SITENAME = u'AM207'
SITEURL = 'http://localhost:8000'

TIMEZONE ="America/New_York"

THEME = '../pelican-bootstrap3-modified'
BOOTSTRAP_THEME = 'flatly'
TWITTER_USERNAME="am207"

DEFAULT_LANG = u'en'
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Class Piazza', 'https://piazza.com/harvard/spring2014/am207/home'),
          ('Numpy', 'http://docs.scipy.org/doc/numpy/reference/'),
          ('Scipy', 'http://docs.scipy.org/doc/scipy/reference/'),
          ('Pandas', 'http://pandas.pydata.org/pandas-docs/dev/'),
          ('Matplotlib', 'http://matplotlib.org/api/index.html'), 
          ('PyMC3', 'https://github.com/pymc-devs/pymc'),        
          ('IACS', 'http://iacs.seas.harvard.edu'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/am207'),)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra']

NEWEST_FIRST_ARCHIVES = True

USE_FOLDER_AS_CATEGORY=False
#MENU
DISPLAY_PAGES_ON_MENU=False
DISPLAY_CATEGORIES_ON_MENU=False

ARTICLEDIR='posts'
PAGEDIR='pages'
PAGE_EXCLUDES=('othermd',)
ARTICLE_EXCLUDES=('pages','othermd',)
#categiries: homework, lecture, lab, project

# if SITEURL[0:4]=='file':
# 	start = SITEURL
# else:
# 	start=""
start = SITEURL

# ('Lectures', "%s/category/lecture.html" % start ),
#           ('Homework', "%s/category/homework.html" % start ),
#           ('Labs', "%s/category/lab.html" % start ),
#           ('Projects', "%s/category/project.html" % start ),
#           ('About AM207', "%s/about-am207.html" % start )

def do_menuitems(start):
  menuitems = [ 		
          ('Schedule', "%s/schedule.html" % start ),
          ('Syllabus', "%s/syllabus.html" % start ),
          ('Policies', "%s/policies.html" % start ),
          ('Resources', "%s/resources.html" % start ),
          ]
  return menuitems

MENUITEMS = do_menuitems(start)

INTERLINKS = {
    'wikipedia_en': 'http://en.wikipedia.org/wiki/',
    'wikipedia_es': 'http://es.wikipedia.org/wiki/',
    'ddg': 'https://duckduckgo.com/?q='
}
PLUGIN_PATH = '../pelican-plugins-activated'
PLUGINS = ['interlinks', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.notebook', 'liquid_tags.include_code',
           'liquid_tags.include_md']

EXTRA_HEADER = open('../notebook_header.html').read().decode('utf-8')

STATIC_PATHS=['static', 'images', 'code', 'notebooks', 'files']

#INDEX_SAVE_AS='index.html'
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

DIRECT_TEMPLATES = ('tags', 'categories', 'authors', 'archives')
