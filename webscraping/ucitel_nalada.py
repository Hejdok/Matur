from bs4 import BeautifulSoup
import requests


url = "https://www.arsenal.com/results"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# matches = soup.find("div", class_="fixtures__match")

away = soup.find("span", class_="scores__score")
home = soup.find("span", class_="scores__score scores__score--arsenal")
arsenal = int(home.text.strip())
opp = int(away.text.strip())
print(f"{home} - {away}")
