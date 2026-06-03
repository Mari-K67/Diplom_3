from selenium.webdriver.common.by import By

class PasswordRecoveryLocators:
    #Кнопка "Восстановить пароль"
    restore_password_button = (By.XPATH, '//a[text()="Восстановить пароль"]')
    #Email поле
    email_field= (By.XPATH, '//input[@name="name"]')
    #Кнопка "Восстановить"
    restore_button = (By.XPATH, '//button[text()="Восстановить"]')
    #поле пароль
    password_field= (By.XPATH, "//label[text()='Пароль']")
    #Кнопка "глаз"
    eye_button = (By.XPATH, '//div[@class="input__icon input__icon-action"]/*[local-name() = "svg"]')
    #поле пароль просвечивающееся
    highlighted_password_field = (By.XPATH, "//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']")
    