# -*- coding: utf-8 -*-
import scrapy
from Meinv.items import MeinvItem

class MeinvSpider(scrapy.Spider):
    name = 'meinv'
    allowed_domains = ['umei.cc/']
    start_urls = ['http://www.umei.cc/tags/meitui.htm']

    def parse(self, response):
        nodes = response.xpath("//div[@class='TypeList']/ul/li/a/@href").extract()
        # print(nodes)
        for node in nodes:
            # yield node

            yield scrapy.Request(node,callback=self.parse_item,dont_filter=True)

    def parse_item(self,response):
        print(response.url)
        # exit()
        # img_src_list = response.xpath("//div[@class='ImageBody']/p/img/@src").extract()
        pages_nums = response.xpath('//div[@class="NewPages"]/ul/li[1]/a/text()').extract()
        pages_nums = int(pages_nums[0][1:-3])+1
        # print(type(int(pages_nums)))
        urls_split = response.url.rsplit('.',1)
        # d_src = MeinvItem()
        for i in range(2, pages_nums):
            m_src = urls_split[0]+ '_'+str(i)+'.'+urls_split[1]
            # d_src['url'] = m_src
            yield scrapy.Request(m_src,callback=self.parse_down,dont_filter=True)
        # print(img_src_list)
        # print('*'*30)
        # m_src = MeinvItem()
        # for src in img_src_list:
        #     m_src['url'] = src
        #     yield m_src
    def parse_down(self,response):
        img_src_list = response.xpath("//div[@class='ImageBody']/p/img/@src").extract()
        m_src = MeinvItem()
        for src in img_src_list:
            m_src['url'] = src
            yield m_src