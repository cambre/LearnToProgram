# Page 90
__author__ = 'Cambre'

import urllib.request
import time

def get_price():
    page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")
    text = page.read().decode("utf-8")
    where = text.find('>$')
    start_of_price = where + 2
    end_of_price = start_of_price + 4
    print("The price of coffee is:")
    return(float(text[start_of_price:end_of_price]))

price_now = input("Do you want to see the price now (Y/N)?")
if price_now == "Y":
    print(get_price())
else:
    price = 99.99
    while price > 4.74:
        time.sleep(15) #900 for 15 minutes
        price = get_price()
    print(price)
