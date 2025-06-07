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
class IngredientData:
        burger_1 = ['61c0c5a71d1f82001bdaaa73', '61c0c5a71d1f82001bdaaa6c',
                    '61c0c5a71d1f82001bdaaa76', '61c0c5a71d1f82001bdaaa79']

        burger_2 = ['61c0c5a71d1f82001bdaaa74', '61c0c5a71d1f82001bdaaa6d',
                    '61c0c5a71d1f82001bdaaa7a', '61c0c5a71d1f82001bdaaa6f']

        invalid_hash_ingredient = '61c0c5a71d1f088005553535'