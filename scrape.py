import requests
from bs4 import BeautifulSoup
from datetime import datetime

URL = 'https://yeeboards.com/shop/'
data = requests.get(URL)

soup = BeautifulSoup(data.content, "html.parser")

results = soup.find("ul", class_='products columns-3')

if results:

    print("Current Kristofer Yee Shop")
    print("")
    counter = 0
    
    right_now = datetime.now()
    dt_string = right_now.strftime("%m/%d/%Y %H:%M:%S")

    li_elements = results.find_all("li")
    
    for li in li_elements:
        product_title = li.find("h2", class_="woocommerce-loop-product__title")
        product_price = li.find("span", class_='woocommerce-Price-amount amount')
        product_link = li.find("a", class_='woocommerce-LoopProduct-link woocommerce-loop-product__link')
        product_avail = li.find("a", class_='button product_type_simple')

        
        if product_title:
            print(f"Product Name: {product_title.text.strip()}")  # strip() to remove leading/trailing whitespace
        if product_price:
            print(f"Product Price: {product_price.text.strip()}")
        print(f"Product Link: {product_link.get('href')}")
        if product_avail:
            print(f"Current Availabiility: {product_avail.text.strip()}")
        else:
            print("No product availability or customizable")
        print("")

        counter += 1

    print(f"{counter} available items in the shop right now", dt_string)
else:
    print("No results found")

