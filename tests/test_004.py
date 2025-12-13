from pages.AdminPage import AdminPage
from pages.LoginPage import LoginPage


def test004(page):
    login_page = LoginPage(page)
    login_page.verify_login_page_displayed()
    login_page.login("admin", "admin123")
    login_page.verify_successful_login()
    admin_page = AdminPage(page)
    admin_page.navigate_to_admin()
    admin_page.enter_username_admin("arvind")
