import requests


class ProjectApi:

    def __init__(self, base_url: str, headers: dict) -> None:
        self.base_url = base_url
        self.headers = headers

    def get_all_projects(self, base_url: str, headers: dict) -> list:
        response = requests.get(base_url, headers=headers)
        return response.json().get("content")

    def create_project(self,
                       base_url: str, project: dict, headers: dict) -> list:
        response = requests.post(base_url, json=project, headers=headers)
        return response.json().get("content")

    def update_project(self, base_url: str, project: dict,
                       project_id: str, headers: dict) -> dict:
        response = requests.put(
            base_url + '/' + str(project_id), json=project, headers=headers)
        return response.status_code

    def get_project_by_id(self, base_url: str, headers: dict,
                          project_id: str) -> dict:
        response = requests.get(base_url + '/' + str(project_id),
                                headers=headers)
        return response.json().get("id")

    def get_project_by_invalid_id(self, base_url: str, headers: dict,
                                  invalid_id: str) -> int:
        response = requests.get(f"{base_url}/{invalid_id}", headers=headers)
        return response.status_code
