from locators import TestLocators
from urls import TestUrl
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestConstructorSections:
    def test_constructor_bread(self, driver):
        driver.get(TestUrl.MAIN_URL)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.TITLE_COLLECT_BURGER))

        driver.find_element(*TestLocators.SAUCE_UNFOCUSED).click()
        driver.find_element(*TestLocators.BREAD_UNFOCUSED).click()

        assert driver.find_element(*TestLocators.BREAD_IN_FOCUS)


    def test_constructor_sauce(self, driver):
        driver.get(TestUrl.MAIN_URL)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.TITLE_COLLECT_BURGER))

        driver.find_element(*TestLocators.SAUCE_UNFOCUSED).click()

        assert driver.find_element(*TestLocators.SAUCE_IN_FOCUS)


    def test_constructor_topping(self, driver):
        driver.get(TestUrl.MAIN_URL)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.TITLE_COLLECT_BURGER))

        driver.find_element(*TestLocators.TOPPING_UNFOCUSED).click()

        assert driver.find_element(*TestLocators.TOPPING_IN_FOCUS)