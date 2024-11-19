from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLocators:

    FORM_AN_ORDER = (By.XPATH, "//button[text()='Оформить заказ']") #Кнопка оформить заказ на главной

    BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']") #Войти на странице /login
    BUTTON_ENTER_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']") #Кнопка Войти в аккаунт на главной
    BUTTON_LK = (By.XPATH, "//*[contains(text(), 'Личный Кабинет')]") #Кнопка Личный кабинет
    BUTTON_FINAL_REGISTRATE = (By.XPATH, "//button[text()='Зарегистрироваться']") #Кнопка Зарегистрироваться на странице с регистрацией
    BUTTON_SMALL_ENTER = (By.XPATH, "//*[contains(@class, 'Auth_link__1fOlj')]") #Кнопка войти на странице /register и /forgot-password
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']") #кнопка Конструктор
    BUTTON_EXIT = (By.XPATH, "//button[text()='Выход']") #кнопка Выход в ЛК
    BUTTON_RESTORE = (By.XPATH, "//button[text()='Восстановить']") #кнопка Востановить на странице Восстановление пароля

    INPUT_NAME = (By.XPATH, "//label[text() = 'Имя']/../input") #поле Имя на странице регистрации
    INPUT_EMAIL = (By.XPATH, "//label[text() = 'Email']/../input") #поле Email
    INPUT_PASSWORD = (By.XPATH, "//label[text() = 'Пароль']/../input") #поле пароль
    WRONG_PASSWORD = (By.XPATH, "//p[text()='Некорректный пароль']") #ввод некоректного пароля

    TITLE_ENTER = (By.XPATH, "//h2[text()='Вход']") #заголовок Вход
    TITLE_COLLECT_BURGER = (By.XPATH, "//h1[text()='Соберите бургер']") #заголовок Соберите бургер

    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2") #лого stellarburgers

    PROFILE = (By.XPATH, "//a[text()='Профиль']") #профиль в ЛК

    SAUCE_UNFOCUSED = (By.XPATH, "//span[text()='Соусы']//parent::div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']")
    SAUCE_IN_FOCUS = (By.XPATH, "//span[text()='Соусы']//parent::div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")
    TOPPING_UNFOCUSED = (By.XPATH, "//span[text()='Начинки']//parent::div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']")
    TOPPING_IN_FOCUS = (By.XPATH, "//span[text()='Начинки']//parent::div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")
    TOPPING_ITEM = (By.XPATH, "//h2[text()='Начинки']")
    BREAD_UNFOCUSED = (By.XPATH, "//span[text()='Булки']//parent::div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']")
    BREAD_IN_FOCUS = (By.XPATH, "//span[text()='Булки']//parent::div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")
