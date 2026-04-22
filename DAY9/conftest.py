import pytest
from playwright.sync_api import Playwright,Page, expect
@pytest.fixture(scope="function")
def set_up_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    yield page
    browser.close()
    
    
@pytest.fixture(scope="session")
def set_tear_down(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    yield page
    browser.close()
    