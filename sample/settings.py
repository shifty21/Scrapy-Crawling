# -*- coding: utf-8 -*-

# Scrapy settings for sample project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'sample'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['sample.spiders']
NEWSPIDER_MODULE = 'sample.spiders'
USER_AGENT = '%s%s' %(BOT_NAME,BOT_VERSION)
DEPTH_LIMIT = 3
DOWNLOAD_DELAY = .5
ITEM_PIPELINES = {'sample.pipelines.SamplePipeline' :1}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'sample (+http://www.yourdomain.com)'
