# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class DouyuItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    room_id = Field()
    game_name = Field()
    show_status = Field()
    child_id = Field()
    isVertical = Field()
    hn = Field()
    specific_status = Field()
    anchor_city = Field()
    show_time = Field()
    subject = Field()
    owner_uid = Field()
    nickname = Field()
    room_name = Field()
    game_url = Field()
    cate_id = Field()
    fans = Field()
    online = Field()
