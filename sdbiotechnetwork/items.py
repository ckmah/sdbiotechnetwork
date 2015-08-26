# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SdbnItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    organization = scrapy.Field()
    address = scrapy.Field()
    description = scrapy.Field()
    company_type = scrapy.Field()
    business_website_address = scrapy.Field()
    business_phone_number = scrapy.Field()
    career_page = scrapy.Field()
    year_founded = scrapy.Field()
    headquarters = scrapy.Field()
    organization_type = scrapy.Field()
    size_range = scrapy.Field()
    geographical_area = scrapy.Field()
