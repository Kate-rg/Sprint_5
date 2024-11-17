from locators import TestLocators
from data import TestData
from urls import TestUrl
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestExitAccount:
    def test_exit_account(self, driver):
        driver.get(TestUrl.MAIN_URL)
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_ENTER_ACCOUNT))

        button_account_enter = driver.find_element(*TestLocators.BUTTON_ENTER_ACCOUNT)
        button_account_enter.click()

        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(*TestData.MAIL)
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(*TestData.PASSWORD)
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_LK))
        personal_account_enter = driver.find_element(*TestLocators.BUTTON_LK)
        personal_account_enter.click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(TestUrl.PROFILE_URL))

        login_title = driver.find_element(*TestLocators.BUTTON_EXIT)
        assert login_title.is_displayed() and login_title.text == 'Выход'

        driver.quit()



