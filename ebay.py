import urllib
import scrapy
import json
import re
import requests

class EbaySpider(scrapy.Spider):
    name = 'ebay'
    allowed_domains = ['api.ebay-kleinanzeigen.de']
    headers = {
        # remove this when using category and location urls
        'X-EBAYK-USECASE': 'results-search',
        'Authorization': 'xxxxx',
        'X-EBAYK-USERID-TOKEN': '',
        'X-EBAYK-APP': '61793c47-b85a-42be-be99-ae408004713a1614272909870',
        'X-ECG-USER-VERSION': '12.9.0',
        'X-ECG-USER-AGENT': 'ebayk-android-app-12.9.0',
        'Host': 'api.ebay-kleinanzeigen.de',
        'Connection': 'close',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'okhttp/4.9.0',
    }
    params = {
        '_in': 'id,title,description,start-date-time,category.id,category.localized_name,ad-address.state,ad-address.zip-code,price,pictures,link,features-active,search-distance,negotiation-enabled,attributes,medias,medias.media,medias.media.title,medias.media.media-link,store-id,store-title',
        'q': 'iphone',  # search query
        'page': '0',  # increment it till you get "numfound":0
        'categoryId': '161',  # after scraping category url choose a catgeory by id
        # when select Reihenfolge > Preis , if you want by Datum remove it
        'sortType': 'PRICE_ASCENDING',
        'adType': 'WANTED',  # angebote - "OFFERED" , Gesuche - "WANTED"
        'posterType': 'PRIVATE',  # gewerblich - "COMMERCIAL" , privat - "PRIVATE"
        'size': '31',  # Default param
        # ( Ort ) location or city  you can get the id by scraping the category url
        'locationId': '13481',
        'pictureRequired': 'false',  # Default param you can make it true
        'distance': '500',  # Umkries Gnaz ( from 1 to 500)
        'minPrice': '100',  # Preis min
        'maxPrice': '500',  # Preis max
        'includeTopAds': 'true',  # Default param don't remove it
        'limitTotalResultCount': 'true',  # Default param you can remove this or keep it
    }


    def start_requests(self):
        # category url
        category = 'https://api.ebay-kleinanzeigen.de/api/categories.json'
        # Locations url
        location = 'https://api.ebay-kleinanzeigen.de/api/locations/top-locations.json'
        # Search Url
        url = f'https://api.ebay-kleinanzeigen.de/api/ads.json?{urllib.parse.urlencode(self.params)}'
    
        yield scrapy.Request(url=url,
                             headers=self.headers,
                             callback=self.parse_results)

    def parse_results(self, response):
        print(json.loads(response.body))

    