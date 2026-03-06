import requests
from bs4 import BeautifulSoup
import pandas as pd

products = []

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

# scrape first 5 pages
for page in range(1, 6):

    url = base_url.format(page)
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    items = soup.find_all("article", class_="product_pod")

    for item in items:

        name = item.h3.a["title"]
        price = item.find("p", class_="price_color").text
        rating = item.p["class"][1]

        products.append({
            "Product_Name": name,
            "Price": price,
            "Category": "Books",
            "Supplier": "BooksToScrape Store",
            "Location": "UK",
            "Rating": rating
        })

df = pd.DataFrame(products)

df.to_csv("products.csv", index=False)
df.to_json("products.json", orient="records", indent=4)

print("Scraping completed")
print("Total records collected:", len(df))