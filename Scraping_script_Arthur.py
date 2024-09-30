# Import de requests & BeatifulSoup

import requests
from bs4 import BeautifulSoup

# Rechercher l'URL

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# Afficher le code HTML de la page

# print(page.text)


soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")


# Afficher après application du parser et indentation

# print(results.prettify())



# Appliquer la casse

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)


# Rechercher dans les balises
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

job_elements = results.find_all("div", class_="card-content")


# Boucle pour afficher les emplois

for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
    links = job_element.find_all("a")

    # Afficher les liens

    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")


# print(python_jobs)


# Message récapitulatif

deb_mess="Il y a "
fin_mess=" emploi Python sur ce site !"
nbr_emploi=len(python_jobs)
message_recap=deb_mess+str(nbr_emploi)+fin_mess
print(message_recap)
