import random
import string

class Url:
    main_url = 'https://qa-stellarburgers.education-services.ru'
    create_user_url = f'{main_url}/api/auth/register'
    delete_user_url = f'{main_url}/api/auth/user'
    forgot_password_url = f'{main_url}/forgot-password'
    reset_password_url = f'{main_url}/reset-password'
    prifile_page_url = f'{main_url}/account/profile'
    oder_histiry_chapter_url = f'{main_url}/account/order-history'
    login_page_url = f'{main_url}/login'
    order_feed_page_url = f'{main_url}/feed'

class UserBody:
    random_field = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
    user_body = {
        "email": f'{random_field}@mail.ru',
        "password": random_field,
        "name": random_field
        }
