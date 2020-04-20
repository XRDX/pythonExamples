import scrapy


class QinziSpider(scrapy.Spider):
    name = "qinzi"

    def start_requests(self):
        for i in range(1, 100):
            url = "https://s.weibo.com/user/&tag=亲子&page=" + str(i)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for card in response.css('div.card'):
            yield {
                "id": card.css('div.avator a')[0].css("a::attr(href)").extract_first(),
                "name": card.css('div.info a::text')[0].extract(),
                "info": card.css("div.info p::text").extract(),
                "fans": card.css('div.info p span a::text')[1].extract(),
            }