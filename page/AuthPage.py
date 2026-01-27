import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthPage:
    """Это класс для страницы авторизации. Он содержит методы
        для взаимодействия с элементами: полем ввода email, пароля,
        кнопкой входа, проверки иконки авторизации и наличия сообщения
        об ошибке при вводе невалидных данных"""

    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://ru.yougile.com/team"
        self.__driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открытие страницы авторизации")
    def open(self) -> None:
        self.__driver.get(self.__url)

    # Локаторы элементов
    login_button = (By.XPATH, '//*[@id="root"]/div/div/div[1]/'
                              'div/div[1]/form/div[3]')
    error_message = (By.XPATH, '//*[@id="root"]/div/div/div[1]/'
                               'div/div[1]/form/div[4]')
    profile_icon = (By.XPATH, '//*[@id="loggedin-container"]/div[2]'
                              '/div[1]/div[7]/div[1]/div[2]')

    @allure.step("Ввод email")
    def enter_email(self, email: str) -> None:
        """Метод находит на странице поле для ввода email, 
        очищает его, заполняет заданным email"""
        email_field = self.__driver.find_element(By.CSS_SELECTOR, 
                                                 '[type="email"]')
        email_field.clear()
        email_field.send_keys(email)

    @allure.step("Ввод пароля")
    def enter_password(self, password: str) -> None:
        """Метод находит на странице поле для ввода пароля, 
        очищает его, заполняет заданным паролем"""
        password_field = self.__driver.find_element(By.CSS_SELECTOR, 
                                                    '[type="password"]')
        password_field.clear()
        password_field.send_keys(password)

    @allure.step("Нажатие кнопки входа")
    def click_login(self) -> None:
        """Метод ожидает, пока кнопка входа станет доступной и кликает ее"""
        login_btn = self.wait.until(EC.element_to_be_clickable
                                    (self.login_button))
        login_btn.click()

    @allure.step("Проверка авторизацию по наличию иконки профиля")
    def is_user_logged_in(self) -> bool:
        """Метод проверяет, что иконка профиля отображается """
        profile = self.wait.until(EC.visibility_of_element_located
                                  (self.profile_icon))
        return profile.is_displayed()

    @allure.step("Получение текущего url")
    def get_current_url(self) -> str:
        """Метод получает текущий url для проверки"""
        return self.__driver.current_url

    @allure.step("Отображение сообщения об ошибке")
    def err_message(self) -> bool:
        """Метод проверяет, что сообщение об ошибке отображается"""
        error_elem = self.wait.until(EC.visibility_of_element_located
                                     (self.error_message))
        return error_elem.is_displayed()

    @allure.step("Получение текста сообщения об ошибке")
    def get_error_message(self) -> str:
        """Метод возвращает текст сообщения об ошибке"""
        error_text = self.__driver.find_element(By.XPATH,
                                                '//*[@id="root"]/div/div/'
                                                'div[1]/div/div[1]/form/div[4]')
        return error_text.text
