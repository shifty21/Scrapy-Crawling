# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import urllib2
def download_pdf(a):
  index = 0
  for i in a :
    f = urllib2.urlopen(i)
    data = f.read()
    name = "pdf" + str(index) + ".pdf"
    index = index + 1
    with open(name,"wb") as code:
      code.write(data)


def download_xls(a):
  index = 0
  for i in a:
    f = urllib2.urlopen(i)
    data = f.read()
    name = "xls" + str(index) + ".xls"
    index = index + 1
    with open(name,"wb") as code:
      code.write(data)

class SamplePipeline(object):
	def process_item(self, obj, spider):
	    download_pdf(obj['pdfs']);
	    download_xls(obj['xls']);
	    
	    return obj
