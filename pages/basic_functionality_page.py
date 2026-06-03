import pytest
import allure
from .base_page import BasePage
from locators.basic_functionality_locators import BasicFunctionalityLocators
from locators.login_locators import LoginLocators

class BasicFunctionalityPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Залогиниться и перейти в раздел Конструктор')
    def login_and_open_constructor(self, email, password):
        self.wait_element_visibility(LoginLocators.profile_chapter)
        self.click(LoginLocators.profile_chapter)
        self.send_keys(LoginLocators.email_field, email)
        self.send_keys(LoginLocators.password_field, password)
        self.click(LoginLocators.login_button)
        self.click(BasicFunctionalityLocators.constructor_chapter)

    @allure.step('Добавить ингредиент в заказ')
    def edit_to_basket(self, ingredient):
        self.drag_element(ingredient, BasicFunctionalityLocators.burger_basket)
