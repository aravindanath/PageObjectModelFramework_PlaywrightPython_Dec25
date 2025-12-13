from pages.LoginPage import LoginPage


def test002(page):
    login_page = LoginPage(page)
    login_page.verify_login_page_displayed()
    login_page.login("admin23", "admin11223")
    login_page.verify_unsuccessful_login()
