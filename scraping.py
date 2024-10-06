import requests
from bs4 import BeautifulSoup

#Choix de l'URL à scrapper et récupération des informations de la page
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

#On sélectionne uniquement les données contenues dans les éléments d'attribut "ResultsContainer" (nos offres d'emploi)
results = soup.find(id="ResultsContainer")

#On sélectionne tout ce dont la class est "card-content"
job_elements = results.find_all("div", class_="card-content")

#On filtre pour n'avoir que les résultats ayant "Python" dans le titre"
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]
#python_job_elements permet de sélectionner l'entièreté de l'élément dont le titre correspond aux conditions de python_jobs

#On réduit uniquement à l'affichage des titres, entreprises et localisation
for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    link_url = job_element.find_all("a")[1]["href"]
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print(f"Apply here: {link_url}\n")