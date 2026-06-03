import allure
from .base_page import BasePage
from locators.order_list_locators import OrderListLocators
from locators.login_locators import LoginLocators
from locators.basic_functionality_locators import BasicFunctionalityLocators

class OrderListPage(BasePage):
    @allure.step('Сделать заказ, как залогиненый пользователь')
    def make_oder(self, email, password, ingredient):
        self.wait_element_visibility(LoginLocators.profile_chapter)
        self.click(LoginLocators.profile_chapter)
        self.send_keys(LoginLocators.email_field, email)
        self.send_keys(LoginLocators.password_field, password)
        self.click(LoginLocators.login_button)
        self.click(BasicFunctionalityLocators.constructor_chapter)
        self.drag_element(ingredient, BasicFunctionalityLocators.burger_basket)
        self.click(OrderListLocators.order_button)
        self.click(OrderListLocators.cross_button_creating_oder)