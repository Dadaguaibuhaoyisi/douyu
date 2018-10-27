# -*- coding: utf-8 -*-
from scrapy import Spider,Request
from douyu.items import DouyuItem
import json


class RoomSpider(Spider):
    name = 'room'
    allowed_domains = ['www.douyu.com']
    start_urls = ['https://www.douyu.com/']
    gameid_url = 'http://open.douyucdn.cn/api/RoomApi/game'
    url = 'http://api.douyutv.com/api/v1/live/{cate}?offset={offset}&limit=30'

    def start_requests(self):#开始爬虫：将所有游戏的分类的json数据传入parse函数
        yield Request(url = self.gameid_url,callback=self.parse)
    def parse(self, response):
        result = json.loads(response.text)
        catemessages = (result['data'])
        # print(catemessages[0])
        # print(catemessages[0]['cate_id'])
        # print(type(catemessages[0]['cate_id']))
        id_name = {}
        for catemessage in catemessages:
            id_name[catemessage['cate_id']] = catemessage['game_name']
        # print(id_name)
        id_name[422]='音乐电台'
        id_name[405]='FM233'
        id_name[441]='连麦互动'
        id_name[447]='情感调频'
        id_name[435]='其他'
        for item in id_name:
            yield Request(url = self.url.format(cate = str(item),offset = str(0)),callback= self.parse_page,dont_filter=True)#offset = str(30*i)
            # yield Request(url = self.url.format(cate = str(item),offset = str(0)),callback= self.page_count(),dont_filter=True)

    def parse_page(self,response):
        url = response.url
        result = json.loads(response.text)
        roommessages = result['data']
        if len(roommessages) > 0:
            for roommessage in roommessages:
                item = DouyuItem()
                for field in item.fields:
                    if field in roommessage.keys():
                        item[field] = roommessage.get(field)
                yield item
        for i in range(1,100):
            yield Request(url = response.url.replace('offset=0','offset='+str(i*30)),callback= self.parse_page,dont_filter=True)

    # def page_count(self,response):
        # for i in range(1,1000):


