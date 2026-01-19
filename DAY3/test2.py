
import re

from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:

    page.goto("https://www.google.com/sorry/index?continue=https://www.google.com/search%3Fq%3Dorangehrm%26oq%3Dorangehrm%26gs_lcrp%3DEgZjaHJvbWUyBggAEEUYOdIBCDM3OThqMGoxqAIAsAIB%26sourceid%3Dchrome%26ie%3DUTF-8%26sei%3DoQhqaaiwDbys4-EPvu61wQk&q=EhAkAUkAHChUQ5mrkP4crB66GKGRqMsGIjCbMh8d-AMudvhKqI8VLeLOgkwaPxh4MNE-n1BJUaiw38k2xJM_DzlRyAbPwOUEU4QyAVJaAUM")



    page.get_by_role("link", name="OrangeHRM: Human Resources").click()

    page.goto("https://www.google.com/search?q=orangehrm&oq=orangehrm&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDM3OThqMGoxqAIAsAIB&sourceid=chrome&ie=UTF-8&sei=oQhqaaiwDbys4-EPvu61wQk")

    page.get_by_role("link", name="OrangeHRM OrangeHRM https://").click()

    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("Admin")

    page.get_by_role("textbox", name="Password").click()

    page.get_by_role("textbox", name="Password").click()

    page.get_by_role("textbox", name="Password").click()

    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()

    page.get_by_role("listitem").filter(has_text="avd bdyg").locator("i").click()

    page.get_by_role("menuitem", name="Logout").click()

    expect(page.locator("form")).to_contain_text("UsernamePassword Login Forgot your password?")
