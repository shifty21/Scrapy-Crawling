# Scrapy-Crawling
Sample Project to crawl a web page for pdf,excels and urls
Steps to get started
1. Install scrapy on windows(via pip) - pip install scrapy
  if pip is not installed install it first via https://pip.pypa.io/en/latest/installing/ .. Download get-pip.py and install using python
  python get-pip.py
2. You might need to install few other packages including lxml , visual c++ .
3. Once everything is setup you can either clone this repo or follow 
   http://doc.scrapy.org/en/latest/intro/tutorial.html

Steps to get this project running and scrapy settings
Directory structure followed

tutorial/
    scrapy.cfg            # deploy configuration file

    tutorial/             # project's Python module, you'll import your code from here
        __init__.py

        items.py          # project items file

        pipelines.py      # project pipelines file

        settings.py       # project settings file

        spiders/          # a directory where you'll later put your spiders
            __init__.py
            ...
1.Replace domain, start_url in sample_spider.py to get the spider pointing to your web page
  You can set the rules to restrict some urls and allow urls you want to crawl in the spyder setting
  rules = (
    Rule(SgmlLinkExtractor(restrict_xpaths=('//body//a/@href'))),
    Rule(SgmlLinkExtractor(allow=('<start_url>',)),callback='parse_item'),
    )
2.Go to root directory and run - scrapy crawl <test-name of the spider>
3.You can use scrapy pipline to append tasks together similar to whats done in this project
  After crawling scrapy calls the tasks in the pipline which are downloading excels and pdfs
  set the pipline in scrapy settings 
  ITEM_PIPELINES = {'sample.pipelines.SamplePipeline' :1}
4.You can set the depth limit up to which scrapy can crawl recursively in scrapy settings
  DEPTH_LIMIT = 3

Ref : http://doc.scrapy.org/en/latest/intro/tutorial.html
