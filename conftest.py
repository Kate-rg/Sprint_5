import pytest
from selenium import webdriver

from data import TestData


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)

    yield driver

    driver.quit()

@pytest.fixture(scope='module')
def test_data():
    return TestData()