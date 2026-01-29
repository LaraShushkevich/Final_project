import allure
import pytest
import requests
from selenium import webdriver
from api.ProjectApi import ProjectApi
from testdata.DataProvider import DataProvider
from configuration.ConfigProvider import ConfigProvider


@pytest.fixture
def driver():
    with allure.step("Открыть и настроить браузер"):
        time_out = ConfigProvider().getint("ui", "time_out")
        driver = webdriver.Chrome()
        driver.implicitly_wait(time_out)
        driver.maximize_window()
        yield driver
    with allure.step("Закрыть браузер"):
        driver.quit()


@pytest.fixture
def headers():
    token = DataProvider().get("token")
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }


@pytest.fixture
def api() -> ProjectApi:
    base_url = ConfigProvider().get_api_url()
    token = DataProvider().get("token")
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    return ProjectApi(base_url, headers)


@pytest.fixture
def project_id(headers):
    base_url = ConfigProvider().get_api_url()
    project = {
        "title": "For use",
        "users": DataProvider().get("users")
    }
    response = requests.post(base_url, json=project, headers=headers)
    project_id = response.json().get("id")
    yield project_id
