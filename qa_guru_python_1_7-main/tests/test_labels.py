import allure
from allure_commons.types import Severity
from selene import browser, by
from selene.support.conditions import be


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "eroshenkoam")
@allure.feature("Задачи в репозитории")
@allure.story("Неавторизованный пользователь пытается получить информацию о работе с allure")
@allure.description("Проверка наличия репозитория")
@allure.link("https://github.com", name="Testing")
@allure.title("Дополнительный шаг с декоратором @allure")
def test_labels_steps(browser_settings):
    @allure.step("Открываем главную страницу")
    def open_main_page():
        browser.open('https://github.com')

    @allure.step("Ищем репозиторий {repository_name}")
    def search_for_repository(repository_name):
        browser.element('[class="search-input"]').click()
        browser.element('[id="query-builder-test"]').type(repository_name).press_enter()

    @allure.step("Переходим на страницу найденного репозитория")
    def go_to_repository():
        browser.element('[class="Text__StyledText-sc-17v1xeu-0 fsOMbO search-match"]').click()

    @allure.step("Проверяем наличие Issue с названием {name}")
    def should_see_request_info(title_name):
        browser.element(by.partial_text(title_name)).should(be.visible)

        open_main_page('/')
        search_for_repository("eroshenkoam/allure-pytest-example")
        go_to_repository()
        should_see_request_info("allure-pytest-example")
