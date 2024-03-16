import requests as rq
from bs4 import BeautifulSoup as bsoup
import csv

response = rq.get("https://www.soq-dz.com/")
soup = bsoup(response.text, 'lxml')
products = soup.findAll("article", {"class": "card"})



with open('prodcuts.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Product', 'Price'])
    for item in products:
        title = item.find("h3", {"class": "card__title"}).text
        price = item.find("strong", {"class": "card__price"}).text
        writer.writerow([title, price])



