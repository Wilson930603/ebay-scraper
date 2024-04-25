import requests

headers = {
    'Host': 'apisd.ebay.com',
    'Connection': 'close',
    'User-Agent': 'eBayAndroid/6.13.0.8',
    'x-ebay-c-marketplace-id': 'EBAY-DE',
    'Content-Type': 'application/json',
    'accept': 'application/json',
    'accept-language': 'en-US',
    'x-ebay-c-request-id': 'rci=ubHmgE1yQoWX',
    'authorization': 'xxxxx',
    'x-ebay-mobile-app-info': 'tz=-4.00;ver=6.13.0.8',
    'x-ebay-vi-prefetch-modules': 'modules=VLS',
    'Accept-Encoding': 'gzip, deflate',
}

params = (
    ('answersVersion', '1'),
    ('_dmd', '1'),
    ('requestedPageLayoutsForMultiLayoutRegion', 'LIST_1_COLUMN,LARGE_1_COLUMN,GRID_2_COLUMN'),
    ('_fcid', '77'),
    ('_nkw', 'lego 42083'),
    ('supportedUxComponentNames', 'ITEM_CARD,PROMOTED_ITEM_CARD,REWRITE_START,TWO_LINE_MESSAGE,BASIC_USER_MESSAGE,BASIC_MESSAGE,BASIC_SELLER_HEADER,ITEMS_CAROUSEL_V3,NAVIGATION_ANSWER_PILL_CAROUSEL,NAVIGATION_IMAGE_ANSWER_CAROUSEL,NAVIGATION_ANSWER_TEXT_LIST,PAGE_TITLE_BAR,C2C_IMAGE_BANNER,CATEGORY_NAV_VERTICAL,EVENTS_IMAGE_BANNER,ITEMS_LIST_VERTICAL,PRODUCTS_VERTICAL,STATUS_BAR_V2,TOGGLE_MESSAGE,ICON_TOGGLE_MESSAGE,FIRST_PARTY_ADS_BANNER,VEHICLE_PARTS_FINDER,MOTORS_TIRE_FINDER,ICON_MESSAGE,ACTION_ERROR,SEED_IMAGE,SAVE_CARD,NATIVE_AFS_ADS,IMAGE_ANSWER_GUIDANCE_CAROUSEL,ASPECTS_IN_RIVER,SPECTRUM_OF_VALUE_CAROUSEL,EEK_ICON,SPONSORED_BADGE'),
)

response = requests.get('https://apisd.ebay.com/experience/search/v1/search_results',
                        headers=headers,
                        params=params,
                        verify=False)
