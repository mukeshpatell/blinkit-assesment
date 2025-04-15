import asyncio
import json
from playwright.async_api import async_playwright
import pandas as pd
from datetime import datetime

# Load lat, long coordinates from CSV for location purpose
def load_coords_from_csv(file_path):
    df = pd.read_csv(file_path)
    return list(zip(df['latitude'], df['longitude']))

# retrive and append product info from response
def extract_product_info(api_json, lat, lon):
    products = []
    snippets = api_json.get("response", {}).get("snippets", [])
    for item in snippets:
        data = item.get("data", {})
        cart_item = data.get("atc_action", {}).get("add_to_cart", {}).get("cart_item", {})
        products.append({
            "date": datetime.now().strftime("%Y-%m-%d"),
            "l1_category": "Munchies",
            "l1_category_id": 1237, # this is l1 category id of munchies (nachos is sub cat of it)
            "l2_category": "Nachos",
            "l2_category_id": 316, #this is l2 category id of nachos
            "store_id": cart_item.get("merchant_id"),
            "variant_id": cart_item.get("product_id"),
            "variant_name": cart_item.get("product_name"),
            "group_id": cart_item.get("group_id"),
            "selling_price": cart_item.get("price"),
            "mrp": cart_item.get("mrp"),
            "in_stock": cart_item.get("unavailable_quantity", 0) == 0,
            "inventory": cart_item.get("inventory"),
            "is_sponsored": False,
            "image_url": cart_item.get("image_url"),
            "brand_id": None,
            "brand": cart_item.get("brand"),
            "latitude": lat,
            "longitude": lon
        })
    return products

# Scrape data for a specific location (Based on Lat's, long's)
async def scrape_location(lat, lon):
    url = "https://blinkit.com/cn/munchies/nachos/cid/1237/316"
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            locale='en-US',
            extra_http_headers={
                "X-G-Location": f"{lat},{lon}",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            }
        )
        page = await context.new_page()
        print(f"Scraping data for latitude: -> {lat}, longitude: {lon}")
        api_response = {}

        async def handle_response(response):
            if "/v1/layout/listing_widgets" in response.url and response.status == 200:
                try:
                    json_data = await response.json()
                    api_response["data"] = json_data
                except Exception as e:
                    print(f"Error parsing response: {e}")

        page.on("response", handle_response)

        try:
            await page.goto(url, timeout=90000, wait_until="domcontentloaded")
            await page.wait_for_timeout(5000)
        except Exception as e:
            print(f"Error loading page for {lat}, {lon}: {e}")
        finally:
            await browser.close()

        if "data" in api_response:
            return extract_product_info(api_response["data"], lat, lon)
        else:
            print(f"No data captured for {lat}, {lon}")
            return []

# Main function to orchestrate functionality.
async def main():
    coordinates = load_coords_from_csv("blinkit_locations.csv")
    all_data = []
    for lat, lon in coordinates:
        try:
            data = await scrape_location(lat, lon)
            all_data.extend(data)
        except Exception as e:
            print(f"Failed to scrape data for {lat}, {lon}: {e}")

    if all_data:
        df = pd.DataFrame(all_data)
        output_path = "blinkit_nachos_products.csv"
        df.to_csv(output_path, index=False)
        print(f"Saved {len(df)} records to '{output_path}'")
    else:
        print("No data scraped.")


asyncio.run(main())