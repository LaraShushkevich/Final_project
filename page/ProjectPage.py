import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class ProjectPage:
    """Это класс для страницы проектов. Он содержит методы
            для открытия страницы и получения текущего url"""

    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://ru.yougile.com/team"
        self.__driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открытие страницы проектов")
    def go_project(self) -> None:
        self.__driver.get(self.__url)
        self.__driver.find_element(By.XPATH,
                                   '//*[@id="loggedin-container"]/div[2]'
                                   '/div[1]/div[7]/div[3]/div[2]').click()

    @allure.step("Получения текущего url")
    def get_current_url(self) -> str:
        return self.__driver.current_url
