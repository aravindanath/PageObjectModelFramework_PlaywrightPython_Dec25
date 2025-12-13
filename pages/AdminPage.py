import logging
from playwright.sync_api import Page
import time

from pages.BasePage import BasePage

logger = logging.getLogger(__name__)


class AdminPage(BasePage):

 # Constructor
    def __init__(self, page: Page):
        super().__init__(page)
        # Remove browser launch from here; browser is managed by the pytest fixture

        self.navigareSideMenu_Selector = '.oxd-icon.bi-chevron-left'
        self.navigatetoAmin_Selector = "//span[text()='Admin' and contains(@class, 'oxd-main-menu-item--name')]"
        self.enterUserName_Selector = "(//input[@class='oxd-input oxd-input--active'])[2]"
        self.navigareSideMenu = self.page.locator(self.navigareSideMenu_Selector)
        self.navigatetoAmin = self.page.locator(self.navigatetoAmin_Selector)
        self.enterUserName = self.page.locator(self.enterUserName_Selector)


    # ---------- page locators ----------





    # ---------- page actions ----------

    def navigate_to_admin(self):
        logger.info("Navigating to Admin page")
        self.navigatetoAmin.first.click()
        time.sleep(2)

    def enter_username_admin(self, username: str):
        logger.info(f"Entering username in Admin page: {username}")
        self.enterUserName.fill(username)
        time.sleep(2)
