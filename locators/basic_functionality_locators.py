from selenium.webdriver.common.by import By

class BasicFunctionalityLocators:
    #Раздел "Конструктор"
    constructor_chapter= (By.XPATH, "//p[normalize-space()='Конструктор']")

    #Раздел "Лента заказов"
    order_feed_chapter= (By.XPATH, '//p[text() = "Лента Заказов"]')

    #пример ингредиента
    ingredient_sample = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")
    
    #счетчик товара в заказе
    ingredient_counter = (By.XPATH,"//p[text()='Флюоресцентная булка R2-D3']/ancestor::a//p[contains(@class, 'counter_counter__num')]")
    
    #заголовок "Детали ингредиента"
    details_title = (By.XPATH, '//h2[text() = "Детали ингредиента"]')

    #кнопка крест
    cross_button = (By.XPATH, "//button[@type='button' and contains(@class, 'Modal_modal__close__TnseK')]")

    #заголовок "Собрать бургер"
    assemble_burger_title = (By.XPATH, "//h1[text()='Соберите бургер']")

    #корзина заказа
    burger_basket = (By.XPATH,"//section[contains(@class,'BurgerConstructor_basket')]")
    
    #кнопка заказать
    order_button = By.XPATH, "//button[contains(text(), 'Оформить заказ')]"
    
    #сообщение об успешно созданном заказе
    oder_message = (By.XPATH, "//p[text()='Ваш заказ начали готовить']")


