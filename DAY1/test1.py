import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_example(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=5000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/")
    page.get_by_role("combobox", name="Search").fill("playwr")
    page.get_by_text("playwright automationSee more").click()
    page.locator("iframe[name=\"a-kagawj18oaqf\"]").content_frame.get_by_role("checkbox", name="I'm not a robot").click()
    page.locator("iframe[name=\"c-kagawj18oaqf\"]").content_frame.locator("[id=\"7\"]").click()
    page.get_by_role("combobox", name="Search").click()
    page.get_by_role("combobox", name="Search").click()
    page.get_by_text("shadowfax ipo").click()

    # ---------------------
    context.close()
    browser.close()