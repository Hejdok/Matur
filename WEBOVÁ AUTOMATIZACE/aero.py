import json
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from os import getenv, path

load_dotenv()

def save_to_json(movie_name, rating):
    data = {
        "movie": movie_name,
        "rating": rating
    }

    if path.exists("data.json"):
        with open("data.json", "r", encoding="utf-8") as f:
            existing = json.load(f)
    else:
        existing = []

    existing.append(data)

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=4, ensure_ascii=False)



def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.kinoaero.cz/?sort=sort-by-data")

        extracted_text = page.text_content(".program__movie-name")
        print("Movie:", extracted_text)

        page.goto("https://www.imdb.com/")
        page.wait_for_timeout(2000)

        page.click(".imdb-header-search__input")
        page.fill(".imdb-header-search__input", extracted_text)
        page.click("#suggestion-search-button")
        page.click(".ipc-title-link-wrapper")

        extracted_rating = page.text_content(".sc-4dc495c1-1")
        print("Rating:", extracted_rating)

        save_to_json(extracted_text, extracted_rating)
        print("Saved to data.json")

        input("Zmáčkni jakoukoliv klávesu pro zavření prohlížeče")
        browser.close()


if __name__ == "__main__":
    main()
