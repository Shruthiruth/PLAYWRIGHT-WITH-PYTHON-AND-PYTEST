
from playwright.sync_api import Page, expect

from ..pages.test2 import HomePage
from ..pages.test1 import LoginPage

def test_logout_functionality(page: Page) -> None:
    login_page = LoginPage(page)
    home_page = HomePage(page)
    
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.password_input.fill("admin123")
    login_page.username_input.fill("Admin")
    login_page.login_button.click()
    
    
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")