import os
from serpapi import GoogleSearch

# Replace 'YOUR_SERPAPI_KEY' with your actual SerpAPI key
API_KEY = ''  # Ensure this is the correct and valid API key

def clean_price(price_str):
    # Remove common currency symbols and commas
    price_str = price_str.replace(',', '').replace('₹', '').replace('$', '').replace('€', '').replace('£', '').strip()
    
    # Attempt to convert the cleaned price to a float
    try:
        return float(price_str)
    except ValueError:
        return None

def get_google_shopping_results(search_term):
    params = {
        "engine": "google",
        "q": search_term,
        "tbm": "shop",
        "gl": "in",  # Set to India
        "hl": "en",  # Language set to English
        "api_key": API_KEY
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

    # Print the entire response for debugging purposes
    print(f"Response: {results}")

    if 'shopping_results' not in results:
        print("Failed to retrieve shopping results.")
        return []
    
    shopping_results = results['shopping_results']

    products = []
    for result in shopping_results:
        product_name = result.get('title', 'N/A')
        product_price = result.get('price', 'N/A')
        source_website = result.get('source', 'N/A')

        # Clean and convert price
        cleaned_price = clean_price(product_price)
        if cleaned_price is not None:
            products.append({
                'name': product_name,
                'price': cleaned_price,
                'source': source_website
            })

    return products

# Example usage
search_term = input("Enter the product you want to search: ")
results = get_google_shopping_results(search_term)

# Filter to show the lowest 5 or 6 priced products
if results:
    # Sort the results by price (lowest first)
    results.sort(key=lambda x: x['price'])
    lowest_results = results[:6]  # Get the lowest 6 results

    for idx, product in enumerate(lowest_results, 1):
        print(f"{idx}. {product['name']}")
        print(f"   - Price: ₹{product['price']}")
        print(f"   - Source: {product['source']}\n")
else:
    print("No products found or failed to retrieve the search results.")
