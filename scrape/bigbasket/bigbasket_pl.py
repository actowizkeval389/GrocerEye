import requests
import json
from typing import List, Dict

def search_bigbasket_products(keyword: str) -> List[Dict]:
    """
    Search BigBasket products by keyword and return simplified product information
    
    Args:
        keyword (str): Search keyword for products
        
    Returns:
        List[Dict]: List of products with name, prices, url, quantity and image
    """
    cookies = {
        'x-entry-context-id': '100',
        'x-entry-context': 'bb-b2c',
        '_bb_locSrc': 'default',
        'x-channel': 'web',
        '_bb_aid': 'MzA4NTgxODk5Nw==',
        '_bb_cid': '1',
        '_bb_vid': 'NzA4MzYyNDgwOTE1Mjk4Nzk4',
        '_bb_nhid': '1723',
        '_bb_dsid': '',
        '_bb_dsevid': '',
        '_bb_bhid': '',
        '_bb_loid': '',
        'csrftoken': 'VmKuatqIR2x41ZmPnh3HiLklgbPy8UGZ9R8SUusBY4Ab8rDJWAYgWqrjbe6ea1C1',
        '_bb_bb2.0': '1',
        'is_global': '1',
        '_bb_addressinfo': '',
        '_bb_pin_code': '',
        '_bb_sa_ids': '10654',
        '_is_tobacco_enabled': '0',
        '_is_bb1.0_supported': '0',
        '_bb_cda_sa_info': 'djIuY2RhX3NhLjEwMC4xMDY1NA==',
        'is_integrated_sa': '0',
        'bb2_enabled': 'true',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        'osmos-enabled': 'true',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        'x-channel': 'BB-WEB',
    }

    params = {
        'type': 'ps',
        'slug': keyword,
        'page': '1',
        'bucket_id': '76',
    }

    try:
        response = requests.get(
            'https://www.bigbasket.com/listing-svc/v2/products', 
            params=params, 
            cookies=cookies, 
            headers=headers
        )
        response.raise_for_status()
        
        data = response.json()
        products = []
        
        if 'tabs' in data and len(data['tabs']) > 0:
            for product in data['tabs'][0]['product_info']['products']:
                # Get MRP and selling price
                mrp = product['pricing']['discount']['mrp']
                selling_price = product['pricing']['discount']['prim_price']['sp']
                
                # Set price display based on whether they're different
                price_display = ""
                if mrp == selling_price:
                    price_display = mrp
                else:
                    price_display = f"MRP: {mrp}, SP: {selling_price}"
                
                # Get image URL (using medium size image)
               
                
                product_info = {
                    'name': product['desc'],
                    'price': price_display,
                    'url': f"https://www.bigbasket.com{product['absolute_url']}",
                    'quantity': product['w'],
                    
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
    results = search_bigbasket_products("milk")
    
    # Print results
    for product in results:
        print("\nProduct Details:")
        print(f"Name: {product['name']}")
        print(f"Price: {product['price']}")
        print(f"Quantity: {product['quantity']}")
        print(f"URL: {product['url']}")