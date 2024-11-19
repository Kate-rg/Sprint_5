
from locators import TestLocators
from data import TestData
from urls import TestUrl
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestSuccessfulLogIn:
    def test_successful_log_in_from_main(self, driver):
        driver.get(TestUrl.MAIN_URL)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_ENTER_ACCOUNT))

        button_account_enter = driver.find_element(*TestLocators.BUTTON_ENTER_ACCOUNT)
        button_account_enter.click()

        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(*TestData.MAIL)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(*TestData.PASSWORD)
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(TestUrl.MAIN_URL))
        form_an_order = driver.find_element(*TestLocators.FORM_AN_ORDER)
        assert form_an_order.is_displayed() and form_an_order.text == 'Оформить заказ'


    def test_successful_log_in_from_main_lk(self, driver):
        driver.get(TestUrl.MAIN_URL)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_ENTER_ACCOUNT))

        personal_account_enter = driver.find_element(*TestLocators.BUTTON_LK)
        personal_account_enter.click()

        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(*TestData.MAIL)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(*TestData.PASSWORD)
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(TestUrl.MAIN_URL))
        form_an_order = driver.find_element(*TestLocators.FORM_AN_ORDER)
        assert form_an_order.is_displayed() and form_an_order.text == 'Оформить заказ'


    def test_successful_log_in_registration_form(self, driver):
        driver.get(TestUrl.REGISTER_URL)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.INPUT_NAME))

        small_enter = driver.find_element(*TestLocators.BUTTON_SMALL_ENTER)
        small_enter.click()

        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(*TestData.MAIL)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(*TestData.PASSWORD)
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(TestUrl.MAIN_URL))
        form_an_order = driver.find_element(*TestLocators.FORM_AN_ORDER)
        assert form_an_order.is_displayed() and form_an_order.text == 'Оформить заказ'


    def test_successful_log_in_forgot_password(self, driver):
        driver.get(TestUrl.FORGOT_PASSWORD_URL)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_RESTORE))

        small_enter = driver.find_element(*TestLocators.BUTTON_SMALL_ENTER)
        small_enter.click()

        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(*TestData.MAIL)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(*TestData.PASSWORD)
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(TestUrl.MAIN_URL))
        form_an_order = driver.find_element(*TestLocators.FORM_AN_ORDER)
        assert form_an_order.is_displayed() and form_an_order.text == 'Оформить заказ'

