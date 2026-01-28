import uuid
import allure
import pytest
from api.ProjectApi import ProjectApi

base_url = "https://ru.yougile.com/api-v2/projects"


@pytest.mark.api
@allure.title("Создание проекта")
@allure.suite("API тесты")
@allure.description("Проверка создания проекта")
@allure.feature("Работа с проектами")
@allure.severity("critical")
def test_create_project(headers, api: ProjectApi):
    project = {
        "title": "New Project",
        "users": {
            "0850e032-1491-4909-969d-949e427e2246": "admin"
        }
    }
    list_before = api.get_all_projects(base_url, headers)
    api.create_project(base_url, project, headers)
    list_after = api.get_all_projects(base_url, headers)
    assert len(list_after) - len(list_before) == 1


@pytest.mark.api
@allure.title("Изменение проекта")
@allure.suite("API тесты")
@allure.description("Проверка возможности редактирования проекта")
@allure.feature("Работа с проектами")
@allure.severity("critical")
def test_update_project(headers: dict, api: ProjectApi, project_id):
    new_title = "Updated Title"
    project = {"title": new_title}
    response = api.update_project(base_url, project, project_id, headers)
    assert response == 200


@pytest.mark.api
@allure.title("Получение проекта по id")
@allure.suite("API тесты")
@allure.description("Проверка возможности получения проекта по id")
@allure.feature("Работа с проектами")
@allure.severity("critical")
def test_get_project_by_id(headers: dict, api: ProjectApi, project_id):
    response = api.get_project_by_id(base_url, headers, project_id)
    assert response == project_id


@pytest.mark.api
@allure.title("Получение проекта по неверному id")
@allure.suite("API тесты")
@allure.description("Негативная проверка")
@allure.feature("Работа с проектами")
@allure.severity("critical")
def test_get_project_by_id_negative(headers: dict, api: ProjectApi):
    invalid_id = str(uuid.uuid4())
    response = api.get_project_by_invalid_id(base_url, headers, invalid_id)
    assert response == 404


@pytest.mark.api
@allure.title("Получение проекта по неверному id")
@allure.suite("API тесты")
@allure.description("Негативная проверка")
@allure.feature("Работа с проектами")
@allure.severity("critical")
def test_update_project_negative_without_id(headers: dict, api: ProjectApi):
    new_title = "New Title"
    project_id = ""
    project = {"title": new_title}
    response = api.update_project(base_url, project, project_id, headers)
    assert response == 404
