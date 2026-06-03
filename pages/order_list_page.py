from .basic_functionality_page import BasicFunctionalityPage
from locators.order_list_locators import OrderListLocators

class OrderListPage(BasicFunctionalityPage):
    def make_oder(self, email, password, ingredient):
        self.login_and_open_constructor(email, password)
        self.edit_to_basket(ingredient)
        self.click(OrderListLocators.order_button)
        self.click(OrderListLocators.cross_button_creating_oder)