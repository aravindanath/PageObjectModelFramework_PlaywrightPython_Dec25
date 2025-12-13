import logging
from playwright.sync_api import Page, expect
import time

from pages.BasePage import BasePage

logger = logging.getLogger(__name__)


class LoginPage(BasePage):

 # Constructor
    def __init__(self, page: Page):
        super().__init__(page)
        # Remove browser launch from here; browser is managed by the pytest fixture
        self.base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.username_input_selector = 'input[name="username"]'
        self.password_input_selector = 'input[name="password"]'
        self.login_button_selector = 'button[type="submit"]'
        self.forgotPassword_link_selector = 'text="Forgot your password?"'
        self.username_input = self.page.locator(self.username_input_selector)
        self.password_input = self.page.locator(self.password_input_selector)
        self.login_button = self.page.locator(self.login_button_selector)
        self.forgotPassword_link = self.page.locator(self.forgotPassword_link_selector)

    # ---------- page locators ----------





    # ---------- page actions ----------
    def login(self, username: str, password: str):
        logger.info(f"Navigating to login page: {self.base_url}")
        self.page.goto(self.base_url)
        logger.info(f"Filling username: {username}")
        self.username_input.fill(username)
        logger.info(f"Filling password: {'*' * len(password)}")
        self.password_input.fill(password)
        logger.info("Clicking login button")
        self.login_button.click()

    # ---------- page verifications ----------
    def verify_login_page_displayed(self):
        logger.info(f"Navigating to login page: {self.base_url}")
        self.page.goto(self.base_url)
        logger.info("Verifying username input is visible")
        self.expect_visible(self.username_input_selector)
        logger.info("Verifying password input is visible")
        self.expect_visible(self.password_input_selector)
        logger.info("Verifying login button is visible")
        self.expect_visible(self.login_button_selector)

    def verify_successful_login(self):
        logger.info("Waiting for dashboard page after login")
        time.sleep(2)
        logger.info("Verifying URL contains dashboard")
        self.expect_url_contains("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

    def verify_unsuccessful_login(self):
        logger.info("Verifying error message for invalid credentials")
        error_message = 'text="Invalid credentials"'
        self.expect_visible(error_message)

    def verify_forgot_password_link(self):
        logger.info("Verifying forgot password link is visible")
        self.expect_visible(self.forgotPassword_link_selector)
        logger.info("Clicking forgot password link")
        self.forgotPassword_link.click()
        logger.info("Verifying URL contains requestPasswordResetCode")
        self.expect_url_contains("https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode")