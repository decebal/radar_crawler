# -*- coding: utf-8 -*-
import scrapy


class QuizSpider(scrapy.Spider):
    name = "quiz"
    allowed_domains = ["footballradar.com/quiz"]
    start_urls = (
        'http://www.footballradar.com/quiz/',
    )

    def parse(self, response):
        pass
