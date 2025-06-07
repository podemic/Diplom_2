import allure
import pytest

from src.constants import Account, Message
from src.helpers import register_new_courier_and_return_response, context
from src.stellar_burgers_api import StellarBurgersAPI


class TestUpdateUser:
    @allure.title('Успешный запрос обновления данных пользователя возвращает код ответа 200 и обновлённые данные')
    def test_update_user_with_authorization(self, delete_user_after_create):
        register_new_courier_and_return_response()
        signin_response = StellarBurgersAPI.login_user(context.get('email'), context.get('password'))
        token = signin_response.json()['accessToken']
        context['email'] = Account.USER_DATA['email']
        context['name'] = Account.USER_DATA['name']
        update_response = StellarBurgersAPI.update_user(token, context['email'], context['name'])
        assert update_response.status_code == 200
        assert update_response.json()['user']['email'] == context['email']
        assert update_response.json()['user']['name'] == context['name']

    @allure.title('Запрос обновления данных пользователя без авторизации возвращает код ответа 401 и message:'
                  ' You should be authorised')
    def test_update_user_without_authorization(self, delete_user_after_create):
        register_new_courier_and_return_response()
        token = None
        update_response = StellarBurgersAPI.update_user(token, context['email'], context['name'])
        assert update_response.status_code == 401
        assert update_response.json()['message'] == Message.MESSAGE_WITHOUT_LOGIN
