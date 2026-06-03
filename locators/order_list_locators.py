from selenium.webdriver.common.by import By

class OrderListLocators:
    #Кнопка "Оформить заказ"
    order_button = By.XPATH, "//button[contains(text(), 'Оформить заказ')]"

    #крест для закрытия окна удачного создания заказа
    cross_button_creating_oder = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")

    #раздел Лента заказов
    oder_list_chapter = (By.XPATH, "//p[text()='Лента Заказов']")

    #первый заказ в списке
    first_oder_in_list = (By.XPATH, '(//ul[contains(@class,"OrderFeed_list")]/*)[1]')

    #заголовок Состав в информации о товаре
    composition = (By.XPATH, "//p[text()='Cостав']")

    #номер заказа в истории
    oder_number_in_history = (By.XPATH, '//p[@class="text text_type_digits-default"]')

    #Счетчик заказов за все время
    all_oder_counter = (By.XPATH, '(//p[contains(@class, "OrderFeed_number")])[1]')

    #Счетчик заказов за сегодня
    today_oder_counter = (By.XPATH, '(//p[contains(@class, "OrderFeed_number")])[2]')

    #Заказ в работе
    oder_in_work_number = (By.XPATH, "//li[contains(@class, 'text') and contains(@class, 'text_type_digits-default') and contains(@class, 'mb-2')]")