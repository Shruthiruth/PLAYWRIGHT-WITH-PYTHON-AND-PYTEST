from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self,page:Page):
        self.page = page
        self.logout_menu = page.get_by_role("listitem").filter(has_text="avd bdyg").locator("i")
        self.logout_button = page.get_by_role("menuitem", name="Logout")
        
    def click_logout_menu(self):
        self.logout_menu.click()