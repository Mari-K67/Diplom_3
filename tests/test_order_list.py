import pytest
import allure
from locators.order_list_locators import OrderListLocators
from locators.basic_functionality_locators import BasicFunctionalityLocators
from locators.profile_locators import ProfileLocators
from pages.order_list_page import OrderListPage
from data import Url
#python -B -m pytest tests/test_order_list.py

class TestOderList:
    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_show_oder_information(self, driver): 
        page = OrderListPage(driver)

        with allure.step('1. перейти в раздел Лента заказов'):
            page.click(OrderListLocators.oder_list_chapter)

        with allure.step('2. кликнуть на заказ'):
            page.click(OrderListLocators.first_oder_in_list)

        assert page.is_displayed(OrderListLocators.composition)

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    @pytest.mark.parametrize("ingredient", [
       BasicFunctionalityLocators.ingredient_sample
       ])
    def test_user_order_visibility(self, driver, create_user, ingredient): 
        page = OrderListPage(driver)

        with allure.step('1. сделать заказ'):
            page.make_oder(create_user['email'], create_user['password'], ingredient)

        with allure.step('2. перейти в раздел История заказов'):
            page.click(ProfileLocators.profile_button)
            page.click(ProfileLocators.oder_history_chapter)

        with allure.step('3. получить номер последнего заказа'):
            history_number = page.get_text(OrderListLocators.oder_number_in_history)

        with allure.step('4. перейти в раздел Лента заказов'):
            page.click(OrderListLocators.oder_list_chapter)

        with allure.step('5. получить номер последнего заказа'):
            number_in_list = page.get_text(OrderListLocators.first_oder_in_list)

        assert history_number in number_in_list

    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    @pytest.mark.parametrize("ingredient", [
       BasicFunctionalityLocators.ingredient_sample
       ])
    def test_all_oder_counter(self, driver, create_user, ingredient): 
        page = OrderListPage(driver)

        with allure.step('1. посмотреть сколько в счетчике за все время заказов'):
            page.click(OrderListLocators.oder_list_chapter)
            page.scroll_to_botton()
            counter_before_oder = int(page.get_text(OrderListLocators.all_oder_counter))

        with allure.step('2. сделать заказ'):
            page.click(BasicFunctionalityLocators.constructor_chapter)
            page.make_oder(create_user['email'], create_user['password'], ingredient)

        with allure.step('3. посмотреть сколько в счетчике за все время заказов'):
            page.click(OrderListLocators.oder_list_chapter)
            page.scroll_to_botton()
            counter_after_oder = int(page.get_text(OrderListLocators.all_oder_counter))

        assert counter_after_oder == counter_before_oder+1

    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    @pytest.mark.parametrize("ingredient", [
       BasicFunctionalityLocators.ingredient_sample
       ])
    def test_today_oder_counter(self, driver, create_user, ingredient): 
        page = OrderListPage(driver)

        with allure.step('1. посмотреть сколько в счетчике за сегодня заказов'):
            page.click(OrderListLocators.oder_list_chapter)
            page.scroll_to_botton()
            counter_before_oder = int(page.get_text(OrderListLocators.today_oder_counter))

        with allure.step('2. сделать заказ'):
            page.click(BasicFunctionalityLocators.constructor_chapter)
            page.make_oder(create_user['email'], create_user['password'], ingredient)

        with allure.step('3. посмотреть сколько в счетчике за сегодня заказов'):
            page.click(OrderListLocators.oder_list_chapter)
            page.scroll_to_botton()
            counter_after_oder = int(page.get_text(OrderListLocators.today_oder_counter))

        assert counter_after_oder == counter_before_oder+1

    @allure.title('После оформления заказа его номер появляется в разделе В работе.')
    @pytest.mark.parametrize("ingredient", [
       BasicFunctionalityLocators.ingredient_sample
       ])
    def test_oder_in_work(self, driver, create_user, ingredient): 
        page = OrderListPage(driver)

        with allure.step('1. сделать заказ'):
            page.make_oder(create_user['email'], create_user['password'], ingredient)

        with allure.step('2. перейти в раздел История заказов'):
            page.click(ProfileLocators.profile_button)
            page.click(ProfileLocators.oder_history_chapter)

        with allure.step('3. получить номер последнего заказа'):
            history_number = page.get_text(OrderListLocators.oder_number_in_history)

        with allure.step('4. перейти в раздел Лента заказов'):
            page.click(OrderListLocators.oder_list_chapter)

        with allure.step('5. получить номер последнего заказа в работе'):
            number_in_work = int(page.get_text(OrderListLocators.oder_in_work_number))

        assert history_number == f'#0{number_in_work}'