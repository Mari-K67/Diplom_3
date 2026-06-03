import allure
from .base_page import BasePage
from locators.profile_locators import ProfileLocators
from locators.login_locators import LoginLocators

class ProfilePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Залогиниться и перейти в Личный кабинет')
    def login_and_head_to_profile_page(self, email, password):
        self.wait_element_visibility(LoginLocators.profile_chapter)
        self.click(LoginLocators.profile_chapter)
        self.send_keys(LoginLocators.email_field, email)
        self.send_keys(LoginLocators.password_field, password)
        self.click(LoginLocators.login_button)
        self.wait_clickable_element(ProfileLocators.profile_button)
        self.click(ProfileLocators.profile_button)
        self.wait_element_visibility(ProfileLocators.name_field)

    @allure.step('Выйти из системы')
    def logout(self):
        self.click(ProfileLocators.logout_button)
        self.wait_element_visibility(ProfileLocators.enter_title)
