import allure
import pytest
import requests
from selenium import webdriver
from api.ProjectApi import ProjectApi


@pytest.fixture
def driver():
    with allure.step("Открыть и настроить браузер"):
        driver = webdriver.Chrome()
        driver.implicitly_wait(4)
        driver.maximize_window()
        yield driver
    with allure.step("Закрыть браузер"):
        driver.quit()


@pytest.fixture
def headers():
    token = "sD+ywZV5dfIyWZonOGrTbIkTTIb9DBhfuoBJhdraOAJYQe0PhFSGCIhCzBcmel47"
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }


@pytest.fixture
def api() -> ProjectApi:
    base_url = "https://ru.yougile.com/api-v2/projects"
    token = "sD+ywZV5dfIyWZonOGrTbIkTTIb9DBhfuoBJhdraOAJYQe0PhFSGCIhCzBcmel47"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    return ProjectApi(base_url, headers)


@pytest.fixture
def project_id(headers) -> str:
    base_url = "https://ru.yougile.com/api-v2/projects"
    project = {
        "title": "For use",
        "users": {
            "0850e032-1491-4909-969d-949e427e2246": "admin"
        }
    }
    response = requests.post(base_url, json=project, headers=headers)
    project_id = response.json().get("id")
    yield project_id
