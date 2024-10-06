import requests
from bs4 import BeautifulSoup

# URL de la page d'accueil
url_base = "https://books.toscrape.com/"

# Fonction pour récupérer toutes les catégories
def get_categories():
    response = requests.get(url_base)
    soup = BeautifulSoup(response.content, "html.parser")
    categories = soup.find("ul", class_="nav nav-list").find("ul").find_all("a")
    
    category_links = {}
    for category in categories:
        category_name = category.text.strip()
        category_url = url_base + category["href"]
        category_links[category_name] = category_url
    return category_links

# Fonction pour récupérer tous les prix de livres dans une catégorie (toutes les pages)
def get_prices_for_category(category_url):
    prices = []
    while True:
        response = requests.get(category_url)
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Récupérer les prix sur la page courante
        books = soup.find_all("article", class_="product_pod")
        for book in books:
            price_text = book.find("p", class_="price_color").text
            price = float(price_text.replace("£", ""))
            prices.append(price)
        
        # Vérifier s'il y a une page suivante
        next_button = soup.find("li", class_="next")
        if next_button:
            next_url = next_button.find("a")["href"]
            category_url = category_url.rsplit("/", 1)[0] + "/" + next_url
        else:
            break
    return prices

# Fonction pour calculer la moyenne des prix d'une liste
def calculate_average(prices):
    if len(prices) == 0:
        return 0
    return sum(prices) / len(prices)

# Récupérer toutes les catégories
categories = get_categories()

# Pour chaque catégorie, récupérer le nombre de livres et la moyenne des prix
for category_name, category_url in categories.items():
    prices = get_prices_for_category(category_url)
    avg_price = calculate_average(prices)
    num_books = len(prices)
    
    print(f"Catégorie: {category_name}")
    print(f"Nombre de livres: {num_books}")
    print(f"Moyenne des prix: £{round(avg_price, 2)}")
    print("-" * 40)
