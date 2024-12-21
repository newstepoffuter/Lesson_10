import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser


def test_github_instructions():
    with allure.step('Открываем главную страницу сайта GitHub'):
        browser.open('https://github.com')

    with allure.step('Ищем репозиторий eroshenkoam/allure-pytest-example'):
        browser.element('[class="search-input"]').click()
        browser.element('[id="query-builder-test"]').type("eroshenkoam/allure-pytest-example").press_enter()

    with allure.step('Переходим на страницу репозитория'):
        browser.element('[class="Text__StyledText-sc-17v1xeu-0 fsOMbO search-match"]').click()

    with allure.step('В репозитории находим allure-pytest-example"'):
        browser.element(by.partial_text('allure-pytest-example')).should(be.visible)
