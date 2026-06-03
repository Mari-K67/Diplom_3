import pytest
import allure
from pages.profile_page import ProfilePage
from locators.profile_locators import ProfileLocators
from data import Url
#python -B -m pytest tests/test_profile.py

class TestProfile:
    @allure.title('Переход в профиль по клику на «Личный кабинет»')
    def test_head_profile_page(self, driver, create_user): 
        page = ProfilePage(driver)

        with allure.step("""
                        1. залогиниться в системе;
                        2. перейти на страницу "Личный кабинет"
                        """):
            page.login_and_head_to_profile_page(create_user['email'], create_user['password'])

        assert page.get_current_url() == Url.prifile_page_url

    @allure.title('Переход в раздел «История заказов»')
    def test_head_oder_history_page(self, driver, create_user): 
        page = ProfilePage(driver)

        with allure.step("""
                        1. залогиниться в системе;
                        2. перейти на страницу "Личный кабинет"
                        """):
            page.login_and_head_to_profile_page(create_user['email'], create_user['password'])
        
        with allure.step('кликнуть на раздел «История заказов»'):
            page.click(ProfileLocators.oder_history_chapter)

        assert page.get_current_url() == Url.oder_histiry_chapter_url
    
    @allure.title('Выход из аккаунта')
    def test_logout(self, driver, create_user): 
        page = ProfilePage(driver)

        with allure.step("""
                        1. залогиниться в системе;
                        2. перейти на страницу "Личный кабинет"
                        """):
            page.login_and_head_to_profile_page(create_user['email'], create_user['password'])
        
        with allure.step('кликнуть на кнопку "Выход"'):
            page.logout()

        assert page.get_current_url() == Url.login_page_url