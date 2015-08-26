# -*- coding: utf-8 -*-
import scrapy

from sdbiotechnetwork.items import SdbnItem

# run by calling "scrapy crawl sdbn -o items.csv" in project directory

class ExampleSpider(scrapy.Spider):
    name = "sdbn"
    allowed_domains = ["sdbn.org"]
    start_urls = ["http://sdbn.org/directory/?action=viewlistings"]

    for i in range(2, 45):
        page = "http://sdbn.org/directory/page/" + str(i) + "/?action=viewlistings"
        start_urls.append(page)

    def parse(self, response):
        for url in response.selector.xpath('//*[@class="listing-actions cf"]/input/@onclick').extract():
            entry = response.urljoin(url[24:-2])
            yield scrapy.Request(entry, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        for sel in response.xpath('//*[normalize-space(@class)="listing-details cf"]'):
            item = SdbnItem()
            item['organization'] = sel.xpath('//*[normalize-space(@class)="field-value wpbdp-field-organizationname wpbdp-field-title"]/span/a/text()').extract()
            item['address'] = sel.xpath('//*[normalize-space(@class)="field-value wpbdp-field-businessaddress wpbdp-field-meta"]/span/*/text()').extract()
            item['description'] = sel.xpath('//*[normalize-space(@class)="field-value wpbdp-field-description wpbdp-field-content"]/span/text()').extract()
            item['company_type'] = sel.xpath('//*[normalize-space(@class)="field-value wpbdp-field-companytype wpbdp-field-category"]/span/a/text()').extract()
            item['business_website_address'] = sel.xpath('//*[normalize-space(@class)="field-value wpbdp-field-businesswebsiteaddress wpbdp-field-meta"]/span/a/text()').extract()
            item['business_phone_number'] = sel.xpath('//*[normalize-space(@class)="field-value wpbdp-field-businessphonenumber wpbdp-field-meta"]/span/text()').extract()
            item['career_page'] = sel.xpath('//*[normalize-space(@class)="field-value wpbdp-field-careerpage wpbdp-field-meta"]/span/a/text()').extract()
            item['year_founded'] = sel.xpath('//*[normalize-space(@class)="field-value wpbdp-field-yearfounded wpbdp-field-meta"]/span/text()').extract()
            item['headquarters'] = sel.xpath('//*[normalize-space(@class)="field-value wpbdp-field-headquarters wpbdp-field-meta"]/span/text()').extract()
            item['organization_type'] = sel.xpath('//*[normalize-space(@class)="field-value wpbdp-field-organizationtype wpbdp-field-meta"]/span/text()').extract()
            item['size_range'] = sel.xpath('//*[normalize-space(@class)="field-value wpbdp-field-sizerange wpbdp-field-meta"]/span/text()').extract()
            item['geographical_area'] = sel.xpath('//*[normalize-space(@class)="field-value wpbdp-field-geographicalarea wpbdp-field-meta"]/span/text()').extract()
            yield item