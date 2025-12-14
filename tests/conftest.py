import pytest
from playwright.sync_api import sync_playwright
import os
import allure

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        page = item.funcargs.get('page', None)
        if page:
            screenshot_dir = os.path.join('tests', 'screenshots')
            os.makedirs(screenshot_dir, exist_ok=True)
            file_name = f"{item.name}.png"
            file_path = os.path.join(screenshot_dir, file_name)
            page.screenshot(path=file_path, full_page=True)
            # Attach screenshot to Allure report
            with open(file_path, "rb") as image_file:
                allure.attach(image_file.read(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            # Attach screenshot to pytest-html report (as a link)
            if hasattr(rep, 'extra'):
                rep.extra.append(f'<a href="{file_path}" target="_blank">Screenshot</a>')
            else:
                rep.extra = [f'<a href="{file_path}" target="_blank">Screenshot</a>']
