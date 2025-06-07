import allure
import pytest

from src.constants import Account, Message
from src.helpers import register_new_courier_and_return_response, context
from src.stellar_burgers_api import StellarBurgersAPI


class TestLoginUser:
    @allure.title('Успешный запрос авторизации пользователя возвращает код ответа 200 и success: True')
    def test_login_with_valid_credentials(self, delete_user_after_create):
        register_new_courier_and_return_response()
        signin_response = StellarBurgersAPI.login_user(context.get('email'), context.get('password'))
        assert signin_response.status_code == 200
        assert signin_response.json()['success'] == True

    @allure.title('Запрос авторизации пользователя без email или password возвращает код ответа 403 и'
                  ' message: email or password are incorrect')
    @pytest.mark.parametrize('email, password',
        [
            (context.get('email'), Account.USER_DATA['password']),
            (Account.USER_DATA['email'], context.get('password')),
        ]
    )
    def test_login_with_invalid_credentials(self, email, password, delete_user_after_create):
        register_new_courier_and_return_response()
        signin_response = StellarBurgersAPI.login_user(email, password)
        assert signin_response.status_code == 401
        assert signin_response.json()["message"] == Message.MESSAGE_INVALID_FIELD_LOGIN
