from bs4 import BeautifulSoup
from myutils.fetcher import fetch

def parse_prom(category_url, maxpages=3):
    products = []

    for page in range(1, maxpages + 1):
        url = f"{category_url}?page={page}"
        print(f"Парсим: {url}")
        html = fetch(url)
        if not html:
            continue

        soup = BeautifulSoup(html, "html.parser")
        items = soup.select('[data-qaid="product_block"]')

        for item in items:
            name = item.select_one('[data-qaid="product_name"]')
            price = item.select_one('[data-qaid="product_price"]')
            link = item.select_one('[data-qaid="product_link"]')

            if name and price and link:
                products.append({
                    "title": name.text.strip(),
                    "price": price.text.strip(),
                    "link": link['href'].strip()
                })

    return products