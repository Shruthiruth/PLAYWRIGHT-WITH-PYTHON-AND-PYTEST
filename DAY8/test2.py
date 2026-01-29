import re
import pytest
from playwright.sync_api import Page, expect

@pytest.mark.skip(reason="not implemented yet")
def test_example(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    expect(page.locator("[data-test=\"username\"]")).to_be_visible()
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"username\"]").press("Tab")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    page.locator("div").filter(has_text="Swag Labs").nth(5).click()

@pytest.mark.xfail(reason="bug")
def test_example_hi(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    expect(page.locator("[data-test=\"username\"]")).to_be_visible()
    page.locator("[data-test=\"usame\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"usernme\"]").press("Tab")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()