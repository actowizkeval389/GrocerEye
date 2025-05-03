import requests
cookies = {
    'deviceId': 's%3Aa2df3660-b8a2-4f21-b515-af5aa5ff53d9.yLzn9bMQXhwVN7iKROMPqSXGMnWXewxPodU6zXKyU1A',
    'tid': 's%3A6935d3ad-9ba6-4b53-a6ac-465acdeb9575.%2BEWcUsB6Hh06JLrxY4HovhvAbU%2BSXQRf1%2BJmKsD6nXI',
    'sid': 's%3Akdy01b00-263f-40aa-8841-a8c05fe9df98.fwjvPfV2UbvgkCDzqAsGkPF93razdIMe%2FOCY%2BP1FXIk',
    'versionCode': '1200',
    'platform': 'web',
    'subplatform': 'dweb',
    'statusBarHeight': '0',
    'bottomOffset': '0',
    'genieTrackOn': 'false',
    'ally-on': 'false',
    'isNative': 'false',
    'strId': '',
    'openIMHP': 'false',
    'webBottomBarHeight': '0',
    '_gcl_au': '1.1.488047290.1746290736',
    '_ga': 'GA1.1.1457189327.1746290736',
    '_fbp': 'fb.1.1746290736600.488869180250175909',
    '_ga_VEG1HFE5VZ': 'GS2.1.s1746290736$o1$g1$t1746290744$j0$l0$h0',
    '_ga_0XZC5MS97H': 'GS2.1.s1746290736$o1$g1$t1746290744$j0$l0$h0',
    '_ga_8N8XRG907L': 'GS1.1.1746290736.1.1.1746290744.0.0.0',
    'aws-waf-token': '228e3b5c-c7bd-469b-a380-9ebd74f4d775:BQoAhvt0y+wZAAAA:XGMCNdmF8HM1Dsd5NAmMu39VPxsIo9+Ud3APi4+lYEMDum5SUQ0s4H0+SI1qvtD3nsAfN7gxsjt73H5rKRwQaDmzcX/o9S9iPeWpAiqhIOYK9DjAzQ6tgbMZUP4h/0TlU16u3ArUF11UEebPWvINM/5yfcZcxLfUY7g+NFW4XEQur8K+elAn9ArExrGVBurNvR8Bn7JBrFucmB/f78N4QOVqO0RflyupCxg5ZI064yzde15zXEqn',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'matcher': 'gec778ebd9g7ebecdc8fdf9',
    'origin': 'https://www.swiggy.com',
    'priority': 'u=1, i',
    'referer': 'https://www.swiggy.com/instamart/search?custom_back=true&query=milk',
    'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    'x-build-version': '2.266.0',
    # 'cookie': 'deviceId=s%3Aa2df3660-b8a2-4f21-b515-af5aa5ff53d9.yLzn9bMQXhwVN7iKROMPqSXGMnWXewxPodU6zXKyU1A; tid=s%3A6935d3ad-9ba6-4b53-a6ac-465acdeb9575.%2BEWcUsB6Hh06JLrxY4HovhvAbU%2BSXQRf1%2BJmKsD6nXI; sid=s%3Akdy01b00-263f-40aa-8841-a8c05fe9df98.fwjvPfV2UbvgkCDzqAsGkPF93razdIMe%2FOCY%2BP1FXIk; versionCode=1200; platform=web; subplatform=dweb; statusBarHeight=0; bottomOffset=0; genieTrackOn=false; ally-on=false; isNative=false; strId=; openIMHP=false; webBottomBarHeight=0; _gcl_au=1.1.488047290.1746290736; _ga=GA1.1.1457189327.1746290736; _fbp=fb.1.1746290736600.488869180250175909; _ga_VEG1HFE5VZ=GS2.1.s1746290736$o1$g1$t1746290744$j0$l0$h0; _ga_0XZC5MS97H=GS2.1.s1746290736$o1$g1$t1746290744$j0$l0$h0; _ga_8N8XRG907L=GS1.1.1746290736.1.1.1746290744.0.0.0; aws-waf-token=228e3b5c-c7bd-469b-a380-9ebd74f4d775:BQoAhvt0y+wZAAAA:XGMCNdmF8HM1Dsd5NAmMu39VPxsIo9+Ud3APi4+lYEMDum5SUQ0s4H0+SI1qvtD3nsAfN7gxsjt73H5rKRwQaDmzcX/o9S9iPeWpAiqhIOYK9DjAzQ6tgbMZUP4h/0TlU16u3ArUF11UEebPWvINM/5yfcZcxLfUY7g+NFW4XEQur8K+elAn9ArExrGVBurNvR8Bn7JBrFucmB/f78N4QOVqO0RflyupCxg5ZI064yzde15zXEqn',
}

params = {
    'pageNumber': '0',
    'searchResultsOffset': '0',
    'limit': '40',
    'query': '',
    'ageConsent': 'false',
    'layoutId': '2671',
    'pageType': 'INSTAMART_PRE_SEARCH_PAGE',
    'isPreSearchTag': 'false',
    'highConfidencePageNo': '0',
    'lowConfidencePageNo': '0',
    'voiceSearchTrackingId': '',
    'storeId': '1374258',
    'primaryStoreId': '1374258',
    'secondaryStoreId': '1392421',
}

json_data = {
    'facets': {},
    'sortAttribute': '',
}

def search_swiggy_instamart(keyword):
    params['query'] = keyword
    
    response = requests.post(
        'https://www.swiggy.com/api/instamart/search',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    
    products = []
    
    try:
        data = response.json()
        if 'data' in data and 'widgets' in data['data']:
            for widget in data['data']['widgets']:
                if 'data' in widget:
                    for item in widget['data']:
                        if 'variations' in item:
                            for variant in item['variations']:
                                product = {
                                    'name': f"{item['brand']} {item['product_name_without_brand']}",
                                    'quantity': variant['quantity'],
                                    'url': f"https://www.swiggy.com/instamart/item/{item['product_id']}",
                                    'price': get_price_display(
                                        variant['price']['store_price'],  # Using store_price as MRP
                                        variant['price'].get('offer_price', variant['price']['store_price'])  # Using offer_price as SP
                                    )
                                }
                                products.append(product)
    except Exception as e:
        print(f"Error parsing response: {e}")
        
    return products

def get_price_display(mrp, sp):
    if mrp == sp:
        return f"{mrp}"
    else:
        return f"MRP: {mrp}, SP: {sp}"

# Example usage
if __name__ == "__main__":
    results = search_swiggy_instamart("milk")
    for product in results:
        print("\nProduct Details:")
        print(f"Name: {product['name']}")
        print(f"Price: {product['price']}")
        print(f"Quantity: {product['quantity']}")
        print(f"URL: {product['url']}")
