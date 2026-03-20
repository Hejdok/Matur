from bs4 import BeautifulSoup
import requests


def main():

    url = "https://www.trebesin.cz"

    response = requests.get(url)

    soup = BeautifulSoup(response.content,  "html.parser")

    all_p = soup.find_all("p")

    # for p in all_p:
    #     print(p.text)

    # gym = soup.find(id="favimagehover-title4")
    # print(gym.text)
    gym2 = soup.select("#favimagehover-title4")
    print(gym2[0].text)

    # gym2 = soup.select_one(".favimagehover-title4")
    # print(gym2.text)

    # for g in gym2:
    #     print(g.get_text)


if __name__ == "__main__":
    main()