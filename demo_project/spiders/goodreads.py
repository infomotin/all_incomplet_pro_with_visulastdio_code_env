import scrapy
from scrapy.loader import ItemLoader
from demo_project.items import QuoteItem
class GoodReadsSpider(scrapy.Spider):
    #identity
    name = 'goodreads' #simple to name this is abale to lunch spider by calling 
    #request
    def start_requests(self):
        url = 'https://www.goodreads.com/quotes?page=1'
        # urls = [
        #     'https://www.goodreads.com/quotes?page=1',
        #     'https://www.goodreads.com/quotes?page=2',
        #     'https://www.goodreads.com/quotes?page=3',
        #     'https://www.goodreads.com/quotes?page=4',
        #     'https://www.goodreads.com/quotes?page=5',
        #     'https://www.goodreads.com/quotes?page=7',
        #     'https://www.goodreads.com/quotes?page=8',
        #     'https://www.goodreads.com/quotes?page=9',
        #     'https://www.goodreads.com/quotes?page=10',
            
        # ]
        # for url in urls:
        yield scrapy.Request(url=url,callback=self.parse)#this callback method are depending on calling type def parse(self,respones): this type of functions 
    # start_urls = [
    #     'https://www.goodreads.com/quotes?page=1',   #also works without functions 
    # ]
    #respones
    def parse(self,respones):
        next_page = respones.selector.xpath("//a[@class='next_page']/@href").extract_first()
        # next_page = respones.xpath("//a[@class='next_page']/@href").extract_first() also workes 
        if next_page is not None:
            next_page_link = respones.urljoin(next_page)
            yield scrapy.Request(url=next_page_link,callback=self.parse)
        for qu in respones.selector.xpath("//div[@class='quote']"):
        #for qu in respones.xpath("//div[@class='quote']"): also workes 
            loder = ItemLoader(item=QuoteItem(),selector=qu,response=respones)
            loder.add_xpath('text',".//div[@class='quoteText']/text()[1]")
            loder.add_xpath('author',".//span[@class='authorOrTitle']")
            loder.add_xpath('tags',".//div[@class='greyText smallText left']/a")
            yield loder.load_item()
            # yield {
            #     'text': qu.xpath(".//div[@class='quoteText']/text()[1]").extract_first(),
                
            #     'author': qu.xpath(".//span[@class='authorOrTitle']/text()").extract_first(),

            #     'tags': qu.xpath(".//div[@class='greyText smallText left']/a/text()").extract(),
            # }
        
        # page_number = respones.url.split("=")[1]
        # # 'https://www.goodreads.com/quotes?page=1',
        # # explain ['https://www.goodreads.com/quotes?page','1']
        # _file = "{0}.html".format(page_number)
        # with open(_file,'wb') as f:
        #     f.write(respones.body)


  