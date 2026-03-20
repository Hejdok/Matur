import json
from playwright.sync_api import sync_playwright
import os


Login = "Jarmil"
Password = "Admin123"

def main():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        
        page = browser.new_page()
        page.goto("https://souhrada.github.io/playwright-exam/")
        page.click('#login')
        page.fill('input#login', Login)
        page.click('#pass')
        page.fill('input#pass', Password)
        page.click('button.login-btn')
        page.locator('.super-secret-text').text_content()
        print(page.locator('.super-secret-text').text_content())


        page.wait_for_timeout(10000)

    browser.close()
    



if __name__ == "__main__":
    main()