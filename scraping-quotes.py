import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By

url_base = "https://quotes.toscrape.com/"

# Accéder à la page de login
driver = webdriver.Firefox()
driver.get("https://quotes.toscrape.com/login")

# Localiser et remplir le champ username
username_input = driver.find_element(By.ID, "username")
username_input.send_keys("test")

# Localiser et remplir le champ mot de passe
password_input = driver.find_element(By.ID, "password")
password_input.send_keys("test") 

# Soumettre le formulaire
password_input.send_keys(Keys.RETURN)

# Attendre que la page se charge
time.sleep(3)
# Maintenant, nous sommes connectés, et nous pouvons accéder aux pages protégées si nécessaire


# Retour à l'URL de base
page=requests.get(url_base)
soup = BeautifulSoup(page.content, "html.parser")

nb_pages = 0
liste_urls = [url_base]
while True :
    bouton_next = soup.find("li", class_="next")
    if bouton_next :
        url_pagesuivante = bouton_next.find("a")["href"]
        url_suivante = url_base.rsplit("/", 1)[0] + "/" + url_pagesuivante
        liste_urls.append(url_suivante)
        page=requests.get(url_suivante)
        soup = BeautifulSoup(page.content, "html.parser")
    else :
        break
print("Nombre de pages du site web : ",len(liste_urls))

# Fermer le navigateur
driver.quit()