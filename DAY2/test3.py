from playwright.sync_api import Playwright, sync_playwright

def test_example(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/")
    print(page.title())
    assert page.title() == "Google"
    # ---------------------
    context.close()
    browser.close()