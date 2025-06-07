import pytest
import allure
import requests

import urls
from data import *
from urls import *

class TestCreateNewAccount:
    @allure.title('Проверка регистрации с валидными кредами')
    @allure.description('Аккаунт создается Faker-ом')
    def test_create_new_account_success(self):
        payload = {
            'email': create_random_email(),
            'password': create_random_password(),
            'name': create_random_username()
        }

        response = requests.post(urls.user_register, data=payload)
        deserials = response.json()
        assert response.status_code == 200
        assert deserials['success'] is True
        assert 'accessToken' in deserials.keys()
        assert 'refreshToken' in deserials.keys()
        assert deserials['user']['email'] == payload['email']
        assert deserials['user']['name'] == payload['name']
        # удаление использованных тестовых данных из базы после теста
        access_token = deserials['accessToken']
        requests.delete(urls.user_delete, headers={'Authorization': access_token})
