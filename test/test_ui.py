import allure
import pytest
from page.AuthPage import AuthPage
from page.ProjectPage import ProjectPage
from testdata.DataProvider import DataProvider


valid_email = DataProvider().get("valid_email")
valid_password = DataProvider().get("valid_password")
invalid_email = DataProvider().get("invalid_email")
empty_password = DataProvider().get("empty_password")


@pytest.mark.ui
@allure.title("Успешная авторизация")
@allure.suite("UI тесты")
@allure.description("Проверка авторизации с валидными данными")
@allure.feature("Авторизация")
@allure.severity("critical")
def test_valid_login(driver):
    auth_page = AuthPage(driver)
    auth_page.open()
    auth_page.enter_email(valid_email)
    auth_page.enter_password(valid_password)
    auth_page.click_login()

    assert auth_page.is_user_logged_in()
    assert auth_page.get_current_url().endswith('team')


@pytest.mark.ui
@allure.title("Неверный email")
@allure.suite("UI тесты")
@allure.description("Проверка авторизации с неверным email")
@allure.feature("Авторизация")
@allure.severity("critical")
def test_invalid_email(driver):
    auth_page = AuthPage(driver)
    auth_page.open()
    auth_page.enter_email(invalid_email)
    auth_page.enter_password(valid_password)
    auth_page.click_login()
    err = auth_page.get_error_message()

    assert err == 'Неверный e-mail или пароль'


@pytest.mark.ui
@allure.title("Пустой пароль")
@allure.suite("UI тесты")
@allure.description("Проверка авторизации с пустым паролем")
@allure.feature("Авторизация")
@allure.severity("critical")
def test_empty_password(driver):
    auth_page = AuthPage(driver)
    auth_page.open()
    auth_page.enter_email(valid_email)
    auth_page.enter_password(empty_password)
    auth_page.click_login()
    err = auth_page.get_error_message()

    assert err == 'Incorrect request'


@pytest.mark.ui
@allure.title("Пустые email и пароль")
@allure.suite("UI тесты")
@allure.description("Проверка авторизации с пустым email и паролем")
@allure.feature("Авторизация")
@allure.severity("critical")
def test_empty_credentials(driver):
    auth_page = AuthPage(driver)
    auth_page.open()
    auth_page.enter_email('')
    auth_page.enter_password('')
    auth_page.click_login()
    err = auth_page.get_error_message()

    assert err == 'Неверный e-mail или пароль'


@pytest.mark.ui
@allure.title("Переход на страницу проектов")
@allure.suite("UI тесты")
@allure.description("Проверка перехода на страницу проектов после авторизации")
@allure.feature("Авторизация")
@allure.severity("critical")
def test_go_projects(driver):
    auth_page = AuthPage(driver)
    auth_page.open()
    auth_page.enter_email(valid_email)
    auth_page.enter_password(valid_password)
    auth_page.click_login()
    auth_page.is_user_logged_in()

    proj_page = ProjectPage(driver)
    proj_page.go_project()

    assert proj_page.get_current_url().endswith('projects')
