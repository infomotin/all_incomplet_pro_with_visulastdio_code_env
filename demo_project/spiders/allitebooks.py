import scrapy 
class AllItEbookSpider(scrapy.Spider):
    #identity
    name = 'allitebooks' #simple to name this is abale to lunch spider by calling 
    #request
    def start_requests(self):
        urls = [
            'http://www.allitebooks.org/page/2/',
            'http://www.allitebooks.org/page/3/',
            'http://www.allitebooks.org/page/4/',
            'http://www.allitebooks.org/page/5/',
            'http://www.allitebooks.org/page/6/',
            'http://www.allitebooks.org/page/7/',
            'http://www.allitebooks.org/page/8/',
            'http://www.allitebooks.org/page/10/',
            'http://www.allitebooks.org/page/9/',
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    #respones
    def parse(self,respones):
        page_number = respones.url.split("/page/")[1]
        # 'http://www.allitebooks.org/page/2',
        # explain ['https://www.goodreads.com/quotes?page','1']
        page_number = page_number.replace('/','')
        print(page_number)
        _file = "allebooks{0}.html".format(page_number)
        with open(_file,'wb') as f:
            f.write(respones.body)


  