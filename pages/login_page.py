from .base_page import BasePage
from locators.login_locators import LoginLocators

class LoginPage(BasePage): 
    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password): 
        self.wait_element_visibility(LoginLocators.profile_chapter)
        self.click(LoginLocators.profile_chapter)
        self.send_keys(LoginLocators.email_field, email)
        self.send_keys(LoginLocators.password_field, password)
        self.click(LoginLocators.login_button)