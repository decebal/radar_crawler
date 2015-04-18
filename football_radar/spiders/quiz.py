# -*- coding: utf-8 -*-
import scrapy
from football_radar.items import FootballRadarItem

class QuizSpider(scrapy.Spider):
    name = "quiz"
    allowed_domains = ["footballradar.com"]
    start_urls = (
        'http://www.footballradar.com/quiz/',
    )
    result = FootballRadarItem()

    def parse(self, response):
        sel = scrapy.Selector(response)
        operation = sel.xpath('//h3/text()').re(r"\{(.*)\}")
        link = sel.xpath('//h3/text()').re(r"here: (.*)\{")

        result = eval(operation[0])
        url = link[0] + str(result)
        self.result['link'] = url

        yield scrapy.Request(url, callback=self.parse_answer)

    def parse_answer(self, response):
        sel = scrapy.Selector(response)
        self.result['body'] = sel.extract()

        yield self.result
