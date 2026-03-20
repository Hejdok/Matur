from bs4 import BeautifulSoup
import requests
import json

url = "https://www.kurzy.cz/kalendar/svatky/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

name_divs = soup.find_all("div", class_="prvni")

svatky_dnes = []

for div in name_divs:
    a_tag = div.find("a")
    if a_tag:
        jmeno = a_tag.get_text(strip=True)
        print("Dnes má svátek:", jmeno)
        svatky_dnes.append(jmeno)


data = {
    "svatek_dnes": svatky_dnes
}

with open("svatek.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Uloženo do svatek.json")