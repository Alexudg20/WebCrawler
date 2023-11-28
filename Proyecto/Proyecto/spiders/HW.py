from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor 

class hotspider(CrawlSpider):
    name = "hw"
    allowed_domains = ["fandom.com"]
    start_urls = ["https://hotwheels.fandom.com/wiki/Hot_Wheels"]

    rules = (
        Rule(LinkExtractor(allow ="/wiki/List_of_2023_Hot_Wheels"), callback= 'parse_item'),
    )

    def parse_item(self, response):
        yield {
            "title": response.css(".headerSort::text").get(),
        }