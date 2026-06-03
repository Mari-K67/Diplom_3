from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementClickInterceptedException
from seletools.actions import drag_and_drop

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    #Метод, чтобы кликнуть на элемент
    def click(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    #ожидание кликабельности элемента
    def wait_clickable_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(locator))

    #Метод, чтобы получить текст элемента
    def get_text(self, locator):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).text

    #проверка видимости элемента
    def is_displayed(self, locator):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).is_displayed()

    #одидание видимости элемента
    def wait_element_visibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
    
    #заполнение поля
    def send_keys(self, locator, value):
        return self.driver.find_element(*locator).send_keys(value) 

    #прокрутка страницы вниз
    def scroll_to_botton(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #получение текущей ссылки
    def get_current_url(self):
        return self.driver.current_url
    
    #поиск элемента
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    #перетаскивание элемента
    def drag_element(self, source, target):
        drag_and_drop(self.driver, self.driver.find_element(*source), self.driver.find_element(*target))