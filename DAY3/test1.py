import re
from playwright.sync_api import expect

def test_example(page):
    page.goto("https://www.google.com")
    expect(page).to_have_title("Google")

    page.get_by_role("combobox", name="Search").fill("playwright automation")
    page.keyboard.press("Enter")
    
    try:
        page.get_by_role("button", name="Accept all").click()
    except:
        print("No CAPTCHA found, continuing...")

    expect(page).to_have_title(re.compile("playwright automation", re.IGNORECASE))