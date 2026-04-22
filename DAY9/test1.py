import re
import pytest
from playwright.sync_api import Playwright,Page, expect

def test_example(set_up_page) -> None:
    page=set_up_page
    page.goto("https://www.saucedemo.com/")
    expect(page.locator("[data-test=\"username\"]")).to_be_visible()
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"username\"]").press("Tab")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    page.locator("div").filter(has_text="Swag Labs").nth(5).click()
    
    
def test_exagmple(set_tear_down) -> None:
    page=set_tear_down
    page.goto("https://www.saucedemo.com/")
    expect(page.locator("[data-test=\"username\"]")).to_be_visible()
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"username\"]").press("Tab")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    page.locator("div").filter(has_text="Swag Labs").nth(5).click()