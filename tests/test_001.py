from pages.LoginPage import LoginPage


def test001(page):
    login_page = LoginPage(page)
    login_page.verify_login_page_displayed()
    login_page.login("admin", "admin1234")
    login_page.verify_successful_login()
