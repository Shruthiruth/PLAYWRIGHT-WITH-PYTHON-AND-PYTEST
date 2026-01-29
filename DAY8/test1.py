import re
from playwright.sync_api import Playwright, sync_playwright , page , expect


def sauce_demo(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    try:
        page = context.new_page()
        page.goto("https://www.saucedemo.com/")
        page.get_by_placeholder("Username").click()
        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").click()
        page.pause()
        page.get_by_placeholder("Password").fill("secret_sauce")
        page.pause()
        page.get_by_role("button", name="Login").click()
        
        print("Login Successful")
    finally:
        context.close()
        browser.close()

        
