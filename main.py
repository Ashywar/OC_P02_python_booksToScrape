import requests
url = "http://books.toscrape.com/index.html"
page = requests.get(url)

# Voir le code html source
print(page.content)