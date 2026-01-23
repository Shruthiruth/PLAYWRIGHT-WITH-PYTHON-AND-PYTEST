import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.bing.com/")
    page.get_by_role("textbox", name="Enter your search here -").click()
    page.get_by_role("textbox", name="Enter your search here -").fill("ethiraj college for women")
    page.get_by_role("option", name="ethiraj college for women"()).click()
    page.get_by_role("searchbox", name="Enter your search here -").click()
    page.get_by_role("searchbox", name="Enter your search here -").click()
    page.get_by_role("searchbox", name="Enter your search here -").press("Enter")
    page.get_by_role("searchbox", name="Enter your search here -").click()
    page.get_by_role("searchbox", name="Enter your search here -").press("Enter")
    page.get_by_role("searchbox", name="Enter your search here -").click()
    page.get_by_text("chennai").click()
    expect(page.get_by_role("searchbox", name="Enter your search here -")).to_be_visible()
