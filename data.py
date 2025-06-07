from help import *


class UsersData:
    email = 'denis_polosukhin_20__777@yandex.ru'
    password = '123456'
    username = 'Денис'

    credentials_with_one_empty_field = [
        {'email': '', #пустой мейл
         'password': create_random_password(),
         'name': create_random_username()
         },
        {'email': create_random_email(),
         'password': '', # пустой пароль
         'name': create_random_username()
         },
        {'email': create_random_email(),
         'password': create_random_password(),
         'name': '' #пустой user_name
         }
    ]