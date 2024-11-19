import random
from locators import TestLocators
from data import TestData
from urls import TestUrl
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestRegistration:
    def test_successful_registration(self, driver):
        driver.get(TestUrl.REGISTER_URL)

        rnd = random.randint(100, 999)
        name= f"Kate_borodina_15_{rnd}"
        mail= f"Kate_borodina_15_{rnd}@ya.ru"
        password = f"sym{rnd}{rnd}"

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.INPUT_NAME))

        driver.find_element(*TestLocators.INPUT_NAME).send_keys(name)
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(mail)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(password)
        button_final_register = driver.find_element(*TestLocators.BUTTON_FINAL_REGISTRATE)
        button_final_register.click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(TestUrl.LOGIN_URL))
        success_registration = driver.find_element(*TestLocators.TITLE_ENTER)

        assert success_registration.is_displayed() and success_registration.text == 'Вход'


    def test_wrong_password_registration(self, driver):
        driver.get(TestUrl.REGISTER_URL)

        rnd = random.randint(100, 999)
        name = f"Kate_borodina_15_{rnd}"
        mail = f"Kate_borodina_15_{rnd}@ya.ru"

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.INPUT_NAME))

        driver.find_element(*TestLocators.INPUT_NAME).send_keys(name)
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(mail)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(TestData.WRONG_PASSWORD)
        button_final_register = driver.find_element(*TestLocators.BUTTON_FINAL_REGISTRATE)
        button_final_register.click()

        wrong_password = driver.find_element(*TestLocators.WRONG_PASSWORD)
        assert wrong_password.is_displayed() and wrong_password.text == 'Некорректный пароль'