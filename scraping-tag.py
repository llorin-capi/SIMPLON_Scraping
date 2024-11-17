import requests
from bs4 import BeautifulSoup
from collections import Counter

url = "https://quotes.toscrape.com/tableful/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Extraction des tags à partir des balises <a> spécifiques
tags = [a.get_text() for a in soup.find_all("a") if "/tableful/tag/" in a.get("href", "")]

# Vérifier si des tags sont trouvés
if tags:
    # Compter les occurrences
    tag_counts = Counter(tags)
    
    # Trouver le tag le plus fréquent
    most_common_tag = tag_counts.most_common(1)[0]
    print(f"Le tag le plus fréquent est '{most_common_tag[0]}' avec {most_common_tag[1]} occurrences.")
else:
    print("Aucun tag trouvé sur la page.")
