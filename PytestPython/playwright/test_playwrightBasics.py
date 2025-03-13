import time

from playwright.sync_api import Page, Playwright, expect


def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("abc")


def test_playwrightShortCut(page: Page):
    page.goto(abc")


#-- #terms  .text-info  tagName
def test_coreLocators(page:Page):
    page.goto("abc")
    page.get_by_label("Username:").fill("abc")
    page.get_by_label("Password:").fill("abc")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()


def test_firefoxBrowser(playwright: Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()
    page.goto("abc")
    page.get_by_label("Username:").fill("abc")
    page.get_by_label("Password:").fill("learnifdfd")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()



















