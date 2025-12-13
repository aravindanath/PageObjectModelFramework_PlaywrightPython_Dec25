from playwright.sync_api import Page, expect


class BasePage:

    # constructor
    def __init__(self, page: Page):
        self.page = page
        self.base_url = getattr(self, 'base_url', None)
        self.default_timeout = 5000  # Set a default timeout in ms

    # ---------- navigation ----------
    def goto(self, path: str = ""):
        url = self.base_url.rstrip("/") + "/" + path.lstrip("/")
        self.page.goto(url)

    # ---------- element helpers ----------
    def click(self, selector: str):
        self.page.locator(selector).click()

    def fill(self, selector: str, text: str):
        self.page.locator(selector).fill(text)

    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).inner_text()

    def is_visible(self, selector: str) -> bool:
        return self.page.locator(selector).is_visible()

    def expect_visible(self, selector: str):
        expect(self.page.locator(selector)).to_be_visible(timeout=self.default_timeout)

    def expect_url_contains(self, value: str):
        expect(self.page).to_have_url(value, timeout=self.default_timeout)
