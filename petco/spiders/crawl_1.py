import scrapy
import json

class Crawl1Spider(scrapy.Spider):
    name = 'crawl_1'
    # allowed_domains = []
    start_urls = ['https://maps.stores.petco.com/api/getAsyncLocations?template=search&level=search&search=10010&radius=100']

    def parse(self, response):
        json_r=response.json().get('maplist',{})
        json_d=str(json_r[25:len(json_r)-7])
        json_d=json.loads(json_d)
        print(json_d)
        

