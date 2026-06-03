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

    driver.get(Url.main_url)

    yield driver

    driver.delete_all_cookies()
    driver.quit()


@pytest.fixture
def create_user():
    body = UserBody.user_body
    response = requests.post(Url.create_user_url, json=body)
    response_data = response.json()
    access_token = response_data.get("accessToken")
   
    yield body

    if access_token:
        requests.delete(Url.delete_user_url, headers={'Authorization': f'{access_token}'})