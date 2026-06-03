import pytest
import allure
from locators.password_recovery_locators import PasswordRecoveryLocators
from pages.password_recovery_page import PasswordRecoveryPage
from data import Url

class TestPasswordRecovery:
    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_open_recovery_password_page_with_email_field(self, driver): 
        page = PasswordRecoveryPage(driver)

        with allure.step("""
                        1. кликнуть на кнопку "Войти в аккаунт";
                        2. кликнуть на кнопку "Восстановить пароль"
                        """):
            page.open_recovery_password_page_with_email_field()

        assert page.get_current_url() == Url.FORGOT_PASSWORD_URL

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_open_recovery_password_page_with_password_field(self, driver, create_user): 
        page = PasswordRecoveryPage(driver)

        with allure.step("""
                        1. кликнуть на кнопку "Войти в аккаунт";
                        2. кликнуть на кнопку "Восстановить пароль"
                        """):
            page.open_recovery_password_page_with_email_field()
        
        with allure.step('3. заполнить поле email'):
            page.send_keys(PasswordRecoveryLocators.email_field, create_user['email'])
        
        with allure.step('4. кликнуть на кнопку "Восстановить"'):   
            page.click(PasswordRecoveryLocators.restore_button)

        with allure.step('5. ожидание перехода на новую страницу (пока поле пароль не станет видимым)'):    
            page.wait_element_visibility(PasswordRecoveryLocators.password_field)
            
        assert page.get_current_url() == Url.RESET_PASSWORD_URL

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивае его')
    def test_click_to_eye_button(self, driver, create_user): 
        page = PasswordRecoveryPage(driver)

        with allure.step("""
                        1. кликнуть на кнопку "Войти в аккаунт";
                        2. кликнуть на кнопку "Восстановить пароль"
                        """):
            page.open_recovery_password_page_with_email_field()

        with allure.step('3. заполнить поле email"'):
            page.send_keys(PasswordRecoveryLocators.email_field, create_user['email'])
        
        with allure.step('4. кликнуть на кнопку "Восстановить"'):
            page.click(PasswordRecoveryLocators.restore_button)

        with allure.step('5. кликнуть по кнопке показать/скрыть пароль'):
            page.click(PasswordRecoveryLocators.eye_button)
            
        assert page.is_displayed(PasswordRecoveryLocators.highlighted_password_field)