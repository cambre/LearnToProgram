# Loyal customer Price
# Only displays when price is under $4.75
# Added 15 second delay.
# Test to branch 1.0

__author__ = 'Cambre'

import urllib.request
import time
price = 99.99
while price > 4.75:
    time.sleep(15) #900 for 15 minutes
    page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")
    text = page.read().decode("utf-8")
    where = text.find('>$')
    start_of_price = where + 2
    end_of_price = start_of_price + 4
    price = float(text[start_of_price:end_of_price])
print("The price of coffee is " + str(price))