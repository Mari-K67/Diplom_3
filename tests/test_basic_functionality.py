import pytest
import allure
from locators.basic_functionality_locators import BasicFunctionalityLocators
from pages.basic_functionality_page import BasicFunctionalityPage
from locators.login_locators import LoginLocators
from data import Url
#python -B -m pytest tests/test_basic_functionality.py

class TestBasicFunctionality:
    @allure.title('Переход на главную страницу по клику на «Конструктор»')
    def test_open_constructor_chapter(self, driver): 
        page = BasicFunctionalityPage(driver)

        with allure.step('1. перейти на страницу входа'):
            page.click(LoginLocators.profile_chapter)

        with allure.step('2. кликнуть на раздел "Конструктор"'):
            page.click(BasicFunctionalityLocators.constructor_chapter)

        assert page.get_current_url() == f'{Url.main_url}/'

    @allure.title('Переход на страницу ленты заказов по клику на «Лента заказов»')
    def test_open_order_feed_chapter(self, driver): 
        page = BasicFunctionalityPage(driver)

        with allure.step('1. кликнуть на раздел "Лента заказов"'):
            page.click(BasicFunctionalityLocators.order_feed_chapter)

        assert page.get_current_url() == Url.order_feed_page_url

    @allure.title('При клике на ингредиент, появляется всплывающее окно c деталями')
    @pytest.mark.parametrize("ingredient", [
       BasicFunctionalityLocators.ingredient_sample
       ])
    def test_click_to_ingredient(self, driver, ingredient): 
        page = BasicFunctionalityPage(driver)

        with allure.step('1. кликнуть на ингредиент'):
            page.click(ingredient)

        assert page.is_displayed(BasicFunctionalityLocators.details_title)

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    @pytest.mark.parametrize("ingredient", [
       BasicFunctionalityLocators.ingredient_sample
       ])
    def test_click_to_cross(self, driver, ingredient): 
        page = BasicFunctionalityPage(driver)

        with allure.step('1. кликнуть на ингредиент'):
            page.click(ingredient)

        with allure.step('2. кликнуть на крестик'):
            page.click(BasicFunctionalityLocators.cross_button)

        assert page.is_displayed(BasicFunctionalityLocators.assemble_burger_title)

    @allure.title('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    @pytest.mark.parametrize("ingredient", [
       BasicFunctionalityLocators.ingredient_sample
       ])
    def test_add_ingredient_to_oder(self, driver, ingredient): 
        page = BasicFunctionalityPage(driver)

        with allure.step('1. добавить ингредиент в заказ'):
            page.edit_to_basket(ingredient)

        assert int(page.get_text(BasicFunctionalityLocators.ingredient_counter)) == 2

    @allure.title('Залогиненный пользователь может оформить заказ')
    @pytest.mark.parametrize("ingredient", [
       BasicFunctionalityLocators.ingredient_sample
       ])
    def test_create_oder(self, driver, create_user, ingredient): 
        page = BasicFunctionalityPage(driver)

        with allure.step("""
                        1. залогиниться;
                        2. перейти в раздел Конструктор
                        """):
            page.login_and_open_constructor(create_user['email'], create_user['password'])

        with allure.step('3. добавить ингредиент в заказ'):
            page.edit_to_basket(ingredient)

        with allure.step('4. нажать кнопку оформить заказ'):
            page.click(BasicFunctionalityLocators.order_button)

        assert page.is_displayed(BasicFunctionalityLocators.oder_message)