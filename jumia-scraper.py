import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Setup Chrome (headless = invisible)
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Storage for all products
data = []
page = 1

print("Starting scraper...")

while True:
    url = f"https://www.jumia.co.ke/flash-sales/?page={page}#catalog-listing"
    print(f"Scraping page {page}...")

    driver.get(url)
    time.sleep(3)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    products = soup.find_all("article", class_="prd _fb _p col c-prd")

    # If no products found, we've gone past the last page
    if not products:
        print(f"No products found on page {page}, stopping.")
        break

    for product in products:
        # Product name
        name_tag = product.find("h3", class_="name")
        name = name_tag.text.strip() if name_tag else "N/A"

        # New price
        new_price_tag = product.find("div", class_="prc")
        new_price = new_price_tag.text.strip() if new_price_tag else "N/A"

        # Old price
        old_price_tag = product.find("div", class_="old")
        old_price = old_price_tag.text.strip() if old_price_tag else "N/A"

        # Discount
        discount_tag = product.find("div", class_="bdg _dsct _sm")
        discount = discount_tag.text.strip() if discount_tag else "N/A"

        # Brand (first word of product name)
        brand = name.split()[0] if name != "N/A" else "N/A"

        # Rating
        rating_tag = product.find("div", class_="stars _s")
        rating = rating_tag.text.strip() if rating_tag else "N/A"

        # Items left
        items_left_tag = product.find("div", class_="stk")
        items_left = items_left_tag.text.strip() if items_left_tag else "N/A"

        data.append({
            "Product Name": name,
            "New Price": new_price,
            "Old Price": old_price,
            "Discount (%)": discount,
            "Brand": brand,
            "Items Left": items_left,
            "Rating": rating,
        })

    print(f"Page {page} done — {len(products)} products collected.")
    page += 1

# Close chrome
driver.quit()

#Save to CSV
df = pd.DataFrame(data)
df.to_csv("jumia_flash_sales.csv", index=False)

print(f"\nAll done! Total products scraped: {len(data)}")
print(df.head())