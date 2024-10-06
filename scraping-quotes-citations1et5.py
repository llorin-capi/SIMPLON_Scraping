from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.get("https://quotes.toscrape.com/js/page/10/")

# Trouver la première citation
premiere_citation = driver.find_element(By.CLASS_NAME, "quote").text
print("Première citation :", premiere_citation)

driver.quit()

print()

# Trouver la cinquième citation d'un site delayed
driver = webdriver.Firefox()
driver.get("https://quotes.toscrape.com/js-delayed/page/5/")
time.sleep(15)

citations = list(driver.find_elements(By.CLASS_NAME, "quote"))
print ("Cinquième citation :", citations[4].text)

driver.quit()