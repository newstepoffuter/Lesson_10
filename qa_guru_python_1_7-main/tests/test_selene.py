from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser


def test_github_instructions(browser_settings):
    browser.open("https://github.com")
    browser.element('[class="search-input"]').click()
    browser.element('[id="query-builder-test"]').type("eroshenkoam/allure-pytest-example").press_enter()
    browser.element('[class="Text__StyledText-sc-17v1xeu-0 fsOMbO search-match"]').click()
    browser.element(by.partial_text('allure-pytest-example')).should(be.visible)
