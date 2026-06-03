from selenium.webdriver.common.by import By

class LoginLocators:
    #Кнопка "Войти"
    login_button= (By.XPATH, "//button[normalize-space()='Войти']")

    #Раздел "Личный кабинет"
    profile_chapter = (By.XPATH, "//p[text()='Личный Кабинет']")

    #Поле пароль
    password_field = (By.XPATH, '//input[@name="Пароль"]')

    #Поле email 
    email_field = (By.XPATH, '//input[@name="name"]')