from pages.LoginPage import LoginPage


def test003(page):
    login_page = LoginPage(page)
    login_page.verify_login_page_displayed()
    login_page.verify_forgot_password_link()
