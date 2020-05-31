# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose,TakeFirst,Join
from w3lib.html import remove_tags
def remove_unicode_text(value):
    return value.replace(u"\u201c",'').replace(u"\u201d",'')
def remove_unicode_n(value):
    return value.replace("\n  ",'').replace("\n    ",'').replace("  ",'')
# class DemoProjectItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass
class QuoteItem(scrapy.Item):
    text = scrapy.Field(
        input_processor = MapCompose(str.strip,remove_unicode_text),
        output_processor = TakeFirst()

    )
    author = scrapy.Field(
        input_processor = MapCompose(remove_tags,remove_unicode_n),
        # input_processor = MapCompose(str.strip,remove_unicode_n),
        output_processor = TakeFirst()

    )
    tags = scrapy.Field(
        input_processor = MapCompose(remove_tags),
        output_processor = Join(',')
    )
   