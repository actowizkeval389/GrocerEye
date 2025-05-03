from curl_cffi import requests
from typing import List, Dict
import json

def search_blinkit_products(keyword: str) -> List[Dict]:
    """
    Search Blinkit products by keyword and return simplified product information
    
    Args:
        keyword (str): Search keyword for products
        
    Returns:
        List[Dict]: List of products with name, prices, url, quantity
    """
    cookies = {
        'gr_1_deviceId': 'a289db69-092f-4478-9e8a-362f60589788',
        '__cf_bm': '17z6pXDJNLs3eKJuyzQOhWDBWmd3tByyY_ehEE7BRFM-1746289643-1.0.1.1-aLvWvuLPdfcUGXm55uAVnQfGhPqWaLOgc.Mr3_l0eF5yU6BHsEotdc.iyLHmKGYlaFOiCaIKowRBR72b_sHt3WdaGyziTyVmu.gP1sXjx2w',
        '__cfruid': 'cad3c095df672e61ab21bd6c845287503e9b874e-1746289643',
        '_cfuvid': 'HWQK6DcD22vYFYusm1L3cvjiAEgA2p27eds1.3ophkU-1746289643444-0.0.1.1-604800000',
        '_gcl_au': '1.1.46749475.1746289627',
        '_gid': 'GA1.2.1633654450.1746289628',
        'gr_1_locality': '1849',
        '_fbp': 'fb.1.1746289629016.475216724159185556',
        'gr_1_lat': '28.465204',
        'gr_1_lon': '77.06159',
        'gr_1_landmark': 'undefined',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'access_token': 'null',
        'app_client': 'consumer_web',
        'app_version': '1010101010',
        'auth_key': 'c761ec3633c22afad934fb17a66385c1c06c5472b4898b866b7306186d0bb477',
        'content-type': 'application/json',
        'device_id': 'a289db69-092f-4478-9e8a-362f60589788',
        'lat': '28.465204',
        'lon': '77.06159',
        'origin': 'https://blinkit.com',
        'priority': 'u=1, i',
        'referer': f'https://blinkit.com/s/?q={keyword}',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    }

    params = {
        'q': keyword,
        'search_type': 'auto_suggest',
    }

    json_data = {
        'applied_filters': None,
        'monet_assets': [{'name': 'ads_vertical_banner', 'processed': 0, 'total': 0}],
        'previous_search_query': keyword,
        'sort': '',
        'vertical_cards_processed': 12,
    }

    try:
        response = requests.post(
            'https://blinkit.com/v1/layout/search',
            params=params,
            cookies=cookies,
            headers=headers,
            json=json_data,
            impersonate="edge99"
        )
        response.raise_for_status()
        
        data = response.json()
        products = []
        
        if data['is_success'] and 'response' in data:
            for snippet in data['response']['snippets']:
                if 'data' in snippet and snippet['widget_type'] == 'product_card_snippet_type_2':
                    product_data = snippet['data']
                    
                    # Extract product information
                    normal_price = float(product_data.get('normal_price', {}).get('text', '0').replace('₹', '').strip())
                    mrp = float(product_data.get('mrp', {}).get('text', '0').replace('₹', '').strip())
                    
                    # Set price display based on whether they're different
                    price_display = ""
                    if mrp == 0.0:
                        price_display = str(normal_price)
                    else:
                        price_display = f"MRP: {mrp}, SP: {normal_price}"
                    
                    product_info = {
                        'name': product_data['name']['text'],
                        'price': price_display,
                        'quantity': product_data.get('variant', {}).get('text', ''),
                        'url': f"https://blinkit.com/prn/{'-'.join(product_data['name']['text'].lower().split())}/prid/{product_data['product_id']}"
                    }
                    products.append(product_info)
                
        return products
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching products: {e}")
        return []
    except (KeyError, json.JSONDecodeError) as e:
        print(f"Error parsing response: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Example search for milk products
    results = search_blinkit_products("milk")
    
    # Print results
    for product in results:
        print("\nProduct Details:")
        print(f"Name: {product['name']}")
        print(f"Price: {product['price']}")
        print(f"Quantity: {product['quantity']}")
        print(f"URL: {product['url']}")