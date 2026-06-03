import pytest
from selenium import webdriver
from data import Url, UserBody
import requests

@pytest.fixture(params=[
    'chrome',
    'firefox'
    ])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
    else:
        raise ValueError(f"Неподдерживаемый браузер: {request.param}")

    driver.get(Url.MAIN_URL)

    yield driver

    driver.delete_all_cookies()
    driver.quit()


@pytest.fixture
def create_user():
    body = UserBody.USER_BODY
    response = requests.post(Url.CREATE_USER_URL, json=body)
    response_data = response.json()
    access_token = response_data.get("accessToken")
   
    yield body

    if access_token:
        requests.delete(Url.DELETE_USER_URL, headers={'Authorization': f'{access_token}'})