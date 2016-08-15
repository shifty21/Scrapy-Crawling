from __future__ import absolute_import
from scrapy.http import Request
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import urllib2
from sample.items import *

#def download_pdf(a):
#  index = 0
#  for i in a :
#    f = urllib2.urlopen(i)
#    data = f.read()
#    name = "pdf" + str(index) + ".pdf"
#   index = index + 1
#    with open(name,"wb") as code:
#      code.write(data)


#def download_xls(a):
#  for i in a:
#    f = urllib2.urlopen(i)
#    data = f.read()
#    name = "xls" + str(index) + ".xls"
#    index = index + 1
#    with open(name,"wb") as code:
#       code.write(data)

class samplespider(CrawlSpider):
  name = "test"
  allowed_domains = ['<domain>']
  start_urls = ["<start_url>"]
  rules = (
    Rule(SgmlLinkExtractor(restrict_xpaths=('//body//a/@href'))),
    Rule(SgmlLinkExtractor(allow=('<start_url>',)),callback='parse_item'),
    )


  def parse_item(self,response):
    x = response.xpath('//a/@href').extract()
    f= open('link.csv','a+')
    obj = SampleItem()
    obj['pdfs'] = []
    obj['xls'] = []
    for i in x:
      if ".pdf" in i :
        if "http" in i:
          obj['pdfs'].append(i)
        else:
          i = "<start_url>" + i
          obj['pdfs'].append(i)
        f.write("%s\n\n"%i)

      elif ".xls" in i:
        if "http" in i:
          obj['xls'].append(i)
        else:
          i = "<start_url>" + i
          obj['xls'].append(i)
        f.write("%s\n\n"%i)

      elif "http" in i:
        yield Request(i, callback=self.parse_item)
        f.write("%s\n\n"%i)
      else:
        f.write("%s\n\n"%i)

    #download_pdf(obj['pdfs']);
    #download_xls(obj['xls']);
    yield obj
   


