# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TopnpiItem(scrapy.Item):
    name = scrapy.Field()
    category = scrapy.Field()
    description = scrapy.Field()
    hospitalAffiliation = scrapy.Field()
    email = scrapy.Field()
    telephone = scrapy.Field()
    reviewer_name = scrapy.Field()
    review_date = scrapy.Field()
    review = scrapy.Field()
    recommend = scrapy.Field()
    url = scrapy.Field()
