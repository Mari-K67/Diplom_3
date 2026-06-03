import random
import string

class Url:
    MAIN_URL = 'https://qa-stellarburgers.education-services.ru'
    CREATE_USER_URL = f'{MAIN_URL}/api/auth/register'
    DELETE_USER_URL = f'{MAIN_URL}/api/auth/user'
    FORGOT_PASSWORD_URL = f'{MAIN_URL}/forgot-password'
    RESET_PASSWORD_URL = f'{MAIN_URL}/reset-password'
    PRIFILE_PAGE_URL = f'{MAIN_URL}/account/profile'
    ODER_HISTIRY_CHAPTER_URL = f'{MAIN_URL}/account/order-history'
    LOGIN_PAGE_URL = f'{MAIN_URL}/login'
    ORDER_FEED_PAGE_URL = f'{MAIN_URL}/feed'

class UserBody:
    RANDOM_FIELD = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
    USER_BODY = {
        "email": f'{RANDOM_FIELD}@mail.ru',
        "password": RANDOM_FIELD,
        "name": RANDOM_FIELD
        }
