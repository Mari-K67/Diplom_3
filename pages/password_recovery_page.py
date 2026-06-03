import allure
from .base_page import BasePage
from locators.login_locators import LoginLocators
from locators.password_recovery_locators import PasswordRecoveryLocators

class PasswordRecoveryPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
    
    @allure.step('Открытие первой страницы изменения пароля с полем email')
    def open_recovery_password_page_with_email_field(self): 
        self.click(LoginLocators.profile_chapter)
        self.scroll_to_botton()
        self.click(PasswordRecoveryLocators.restore_password_button)