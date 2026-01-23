import re

from playwright.sync_api import Page, expect

def test_example(page: Page) -> None:
    page.goto("https://swaglabs.in/")
    page.locator("(//a[text()='Home'])[1]").click()
    page.locator("(//a[text()='About Us'])[1]").click()
    expect(page).to_have_url("https://swaglabs.in/about-us/")
