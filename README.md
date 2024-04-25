# Reselling Scraper 

## Ebay Reverse

- The main endpoint is `https://api.ebay-kleinanzeigen.de`
- you need two Ids as params to do your search 
1. **catgoryId** : crawl this endpoint `https://api.ebay-kleinanzeigen.de/api/categories.json` to get the Id of each category ( same Headers just remove `X-EBAYK-USECASE': 'results-search`
2. **locationId** : crawl this endpoint `https://api.ebay-kleinanzeigen.de/api/locations/top-locations.json` to get the Id of each city ( headers same as category)
- the most important endpoint is **search** `https://api.ebay-kleinanzeigen.de/api/ads.json?` add params with 
`urllib.parse.urlencode(self.params)`
- we have default params like :
```
'_in': 'id,title,description,start-date-time,category.id,category.localized_name,ad-address.state,ad-address.zip-code,price,pictures,link,features-active,search-distance,negotiation-enabled,attributes,medias,medias.media,medias.media.title,medias.media.media-link,store-id,store-title',
'size': '31',# Default param
'pictureRequired': 'false',# Default param you can make it true
'includeTopAds': 'true', # Default param
'limitTotalResultCount': 'true',# Default param
```
- and we have filters params like :
```
'q': 'iphone',# search query 
'page': '0',# increment it till you get "numfound":0
'categoryId': '161',# after scraping category url choose a catgeory by id 
'sortType': 'PRICE_ASCENDING',# when select Reihenfolge > Preis , if you want by Datum remove it 
'adType': 'WANTED',# angebote - "OFFERED" , Gesuche - "WANTED"
'posterType': 'PRIVATE', # gewerblich - "COMMERCIAL" , privat - "PRIVATE"
'locationId': '13481',# ( Ort ) location or city  you can get the id by scraping the category url
'distance': '500', # Umkries Gnaz ( from 1 to 500)
'minPrice': '100', # Preis min
'maxPrice': '500', # Preis max
```