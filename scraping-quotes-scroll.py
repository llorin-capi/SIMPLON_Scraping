import time
from selenium import webdriver
from selenium.webdriver.common.by import By

## Question 2 : Combien de citations contient ce site web?

url_q2 = "https://quotes.toscrape.com/scroll"
driver = webdriver.Firefox()
driver.get(url_q2)

# On scroll jusqu'en bas de la page
derniere_longueur = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # on fait défiler jusqu'en bas
    time.sleep(1) # on attend que ça charge
    nouvelle_longueur = driver.execute_script("return document.body.scrollHeight") # on récupère la nouvelle valeur de la longueur de la page
    if nouvelle_longueur == derniere_longueur: # on compare les longueurs pour voir si on est descendu ou pas
         break
    derniere_longueur = nouvelle_longueur

# On compte combien de citations ont été trouvées
citations = driver.find_elements(By.CLASS_NAME, "quote")
nb_citations = len(citations)
print("Nombre de citations :", nb_citations)

# Fermer le navigateur
driver.quit()