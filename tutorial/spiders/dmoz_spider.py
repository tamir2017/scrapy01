import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ['dmoztools.net']
    start_urls = [
        'http://dmoztools.net/Computers/Programming/Languages/Python/Books/',
        'http://dmoztools.net/Computers/Programming/Languages/Python/Resources/'
        ]
    def parse(self, response):
        sel = scrapy.selector.Selector(response)
        sites = sel.xpath('//div[@class="title-and-desc"]')
        for site in sites:
            title = site.xpath('a/div/text()').extract()
            link = site.xpath('a/@href').extract()
            desc = site.xpath('div/text()').extract()
            print(title, link, desc)
