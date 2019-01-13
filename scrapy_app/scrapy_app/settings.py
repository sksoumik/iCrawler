
import os
import sys


# DJANGO INTEGRATION

sys.path.append(os.path.dirname(os.path.abspath('.')))
# Do not forget the change iCrawler part based on your project name
os.environ['DJANGO_SETTINGS_MODULE'] = 'iCrawler.settings'

# This is required only if Django Version > 1.8
import django
django.setup()

BOT_NAME = 'scrapy_app'

SPIDER_MODULES = ['scrapy_app.spiders']
NEWSPIDER_MODULE = 'scrapy_app.spiders'



ROBOTSTXT_OBEY = True


