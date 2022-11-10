import requests
from bs4 import BeautifulSoup
import csv


url = "http://books.toscrape.com/index.html"
page = requests.get(url)

# Voir le code html source

soup = BeautifulSoup(page.content, 'html.parser')

titres = soup.find_all("h3")
prices = soup.find_all("p", class_="price_color")

titre_text = []

for titre in titres:
    titre_text.append(titre.string)

price_text = []

for price in prices:
    price_text.append(price.string)

header = ['titre, prix']    
with open('csv_file.csv', "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(header)
    for titre, price in zip(titre_text, price_text):
        writer.writerow([titre, price])
