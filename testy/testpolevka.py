from bs4 import BeautifulSoup
import requests
import json


def main():
    url = "https://souhrada.github.io/bsoup-exam/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser") #hodí nám to soubor v html a my pak si jen vybereme co z toho chceme
    ingre = soup.select('.stuff')
    print(ingre[0].text)
    print(ingre[1].text)
    print(ingre[2].text)
    print(ingre[3].text)

    # json.dump(ingre, recept.json, indent=4)
    # json.load(recept.json)

if __name__ == "__main__":
    main()