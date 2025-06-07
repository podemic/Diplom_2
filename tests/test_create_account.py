import pytest
import allure
import requests
from data import *
from urls import *

class TestCreateNewAccount:
    @allure.title('Проверка регистрации с валидными кредами')
    @allure.description('Аккаунт создается Faker-ом, потом проверяем ответ от сервера')
    def test_create_new_account_success(self):
        payload = {
            'email': create_random_email(),
            'password': create_random_password(),
            'name': create_random_username()
        }
        response = requests.post(Urls.user_register, data=payload)
        json_response = response.json()
        assert response.status_code == 200
        assert json_response['success'] is True
        assert 'accessToken' in json_response.keys()
        assert 'refreshToken' in json_response.keys()
        assert json_response['user']['email'] == payload['email']
        assert json_response['user']['name'] == payload['name']

    @allure.title('Проверка регистрации с существующим в БД email-ом')
    @allure.description('Используется email уже зарегистрированного аккаунта.')
    def test_registration_login_taken_failed_submit(self):
            payload = {
                'email': UsersData.email,
                'password': create_random_password(),
                'name': create_random_username()
            }
            response = requests.post(Urls.user_register, data=payload)
            assert response.status_code == 403 and response.json() == {'success': False,
                                                                       'message': 'User already exists'}

    @allure.title('Проверка ответа на запрос регистрации с незаполненым полем')
    @allure.description('По очереди отправляем запросы,где не заполнено одно из полей — email, passwd или name.')
    @pytest.mark.parametrize('credentials', UsersData.credentials_with_one_empty_field)
    def test_registration_one_required_field_is_empty_failed_submit(self, credentials):
        response = requests.post(Urls.user_register, data=credentials)
        assert (response.status_code == 403 and response.json() ==
                {'success': False, 'message': 'Email, password and name are required fields'})
