from selenium.webdriver.common.by import By

class ProfileLocators:
    #Кнопка "Личный кабинет"
    profile_button = (By.XPATH, "//p[text()='Личный Кабинет']")

    #Раздел "История заказов"
    oder_history_chapter = (By.XPATH, "//a[@href='/account/order-history' and text()='История заказов']")

    #Раздел "Выход"
    logout_button = (By.XPATH, '//button[text() = "Выход"]')

    #поле Имя 
    name_field = (By.XPATH, "//input[@type='text' and @name='Name']")

    #Заголовок страницы "Вход"
    enter_title = (By.XPATH, "//h2[normalize-space()='Вход']")