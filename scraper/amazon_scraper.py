from playwright.sync_api import sync_playwright
import pandas as pd
import time

def scrape_amazon(query="luggage", max_products=10):
    products = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(f"https://www.amazon.in/s?k={query}")

        page.wait_for_timeout(3000)

        items = page.query_selector_all("div.s-main-slot div[data-component-type='s-search-result']")

        for item in items[:max_products]:
            try:
                title = item.query_selector("h2").inner_text()
                price = item.query_selector(".a-price-whole").inner_text()
                rating = item.query_selector(".a-icon-alt").inner_text()

                products.append({
                    "title": title,
                    "price": price,
                    "rating": rating
                })

            except:
                continue

        browser.close()

    df = pd.DataFrame(products)
    df.to_csv("data/raw/products.csv", index=False)
    print("Scraping done!")

if __name__ == "__main__":
    scrape_amazon()
    