from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor 

class myspider(CrawlSpider):
    name = "Rest"
    allowed_domains = ["reddit.com"]
    start_urls = ["https://www.reddit.com/r/news/"]

    rules = (
        Rule(LinkExtractor(allow ="._1oQyIsiPHYt6nx7VOmd1sz"), callback= 'parse_item'),
    )

    def parse_item(self, response):
        yield {
            "title": response.css("._3wqmjmv3tb_k-PROt7qFZe h3::text").get(),
        }