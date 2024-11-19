from locators import TestLocators
from data import TestData
from urls import TestUrl
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestJumpFromAccountToConstructor:
    def test_jump_from_acc_to_constructor(self, driver):
        driver.get(TestUrl.MAIN_URL)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_ENTER_ACCOUNT))

        button_account_enter = driver.find_element(*TestLocators.BUTTON_ENTER_ACCOUNT)
        button_account_enter.click()

        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(*TestData.MAIL)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(*TestData.PASSWORD)
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_LK))
        personal_account_enter = driver.find_element(*TestLocators.BUTTON_LK)
        personal_account_enter.click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(TestUrl.PROFILE_URL))

        button_constructor = driver.find_element(*TestLocators.BUTTON_CONSTRUCTOR)
        button_constructor.click()

        title_collect_burger = driver.find_element(*TestLocators.TITLE_COLLECT_BURGER)
        assert title_collect_burger.is_displayed() and title_collect_burger.text == 'Соберите бургер'


    def test_jump_from_acc_to_constructor_by_logo(self, driver):
        driver.get(TestUrl.MAIN_URL)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_ENTER_ACCOUNT))

        button_account_enter = driver.find_element(*TestLocators.BUTTON_ENTER_ACCOUNT)
        button_account_enter.click()

        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(*TestData.MAIL)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(*TestData.PASSWORD)
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_LK))
        personal_account_enter = driver.find_element(*TestLocators.BUTTON_LK)
        personal_account_enter.click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(TestUrl.PROFILE_URL))

        logo = driver.find_element(*TestLocators.LOGO)
        logo.click()

        title_collect_burger = driver.find_element(*TestLocators.TITLE_COLLECT_BURGER)
        assert title_collect_burger.is_displayed() and title_collect_burger.text == 'Соберите бургер'
