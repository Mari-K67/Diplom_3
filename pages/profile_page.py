from .login_page import LoginPage
from locators.profile_locators import ProfileLocators

class ProfilePage(LoginPage):
    def __init__(self, driver):
        self.driver = driver

    def login_and_head_to_profile_page(self, email, password):
        self.login(email, password)
        self.wait_clickable_element(ProfileLocators.profile_button)
        self.click(ProfileLocators.profile_button)
        self.wait_element_visibility(ProfileLocators.name_field)

    def logout(self):
        self.click(ProfileLocators.logout_button)
        self.wait_element_visibility(ProfileLocators.enter_title)
