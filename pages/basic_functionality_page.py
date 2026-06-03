import pytest
from .login_page import LoginPage
from locators.basic_functionality_locators import BasicFunctionalityLocators

class BasicFunctionalityPage(LoginPage):
    def __init__(self, driver):
        self.driver = driver

    def login_and_open_constructor(self, email, password):
        self.login(email, password)
        self.click(BasicFunctionalityLocators.constructor_chapter)

    def edit_to_basket(self, ingredient):
        self.drag_element(ingredient, BasicFunctionalityLocators.burger_basket)
