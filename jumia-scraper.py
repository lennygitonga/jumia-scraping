import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


driver.get("https://www.jumia.co.ke/flash-sales/")


time.sleep(5)


soup = BeautifulSoup(driver.page_source, "html.parser")


products = soup.find_all("article", class_="prd")

print(f"Found {len(products)} products")


data = []

for product in products:
    
    name_tag = product.find("h3", class_="name")
    name = name_tag.text.strip() if name_tag else "N/A"

    
    new_price_tag = product.find("div", class_="prc")
    new_price = new_price_tag.text.strip() if new_price_tag else "N/A"

    
    old_price_tag = product.find("div", class_="old")
    old_price = old_price_tag.text.strip() if old_price_tag else "N/A"

    
    discount_tag = product.find("div", class_="bdg _dsct")
    discount = discount_tag.text.strip() if discount_tag else "N/A"

    
    brand = name.split()[0] if name != "N/A" else "N/A"

    
    rating_tag = product.find("div", class_="stars _s")
    rating = rating_tag.text.strip() if rating_tag else "N/A"

    
    items_left_tag = product.find("div", class_="clb")
    items_left = items_left_tag.text.strip() if items_left_tag else "N/A"

    
    time_left_tag = product.find("div", class_="cntdwn")
    time_left = time_left_tag.text.strip() if time_left_tag else "N/A"

    data.append({
        "Product Name": name,
        "New Price": new_price,
        "Old Price": old_price,
        "Discount (%)": discount,
        "Brand": brand,
        "Items Left": items_left,
        "Rating": rating,
        "Time Left": time_left
    })