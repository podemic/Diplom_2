import allure
import pytest

from src.constants import Message, Account
from src.helpers import register_new_courier_and_return_response, context
from src.stellar_burgers_api import StellarBurgersAPI


class TestCreateUser:
    @allure.title('Успешный запрос создание пользователя возвращает код ответа 200 и success: True')
    def test_create_unique_user(self, delete_user_after_create):
        signup_response = register_new_courier_and_return_response()
        assert signup_response.status_code == 200
        assert signup_response.json()['success'] == True

    @allure.title('Попытка создания уже зарегистрированного пользователя возвращает код ответа 403 и'
                  ' message: User already exists')
    def test_create_existing_user(self, delete_user_after_create):
        signup_response = register_new_courier_and_return_response()
        assert signup_response.status_code == 200
        assert signup_response.json()['success'] == True
        signup_response_two = StellarBurgersAPI.create_user(context.get('email'), context.get('password'), context.get('name'))
        assert signup_response_two.status_code == 403
        assert signup_response_two.json()['success'] == False
        assert signup_response_two.json()['message'] == Message.MESSAGE_EXISTING_SIGNUP

    @allure.title('Попытка создания пользователя без email, password или name возвращает код ответа 403 и message:'
                  ' Email, password and name are required fields')
    @pytest.mark.parametrize('email, password, name',
        [
            ('', Account.USER_DATA['password'], Account.USER_DATA['name']),
            (Account.USER_DATA['email'], '', Account.USER_DATA['name']),
            (Account.USER_DATA['email'], Account.USER_DATA['password'], ''),
        ]
    )
    def test_create_user_with_missing_fields_email(self, email, password, name):
        signup_response_two = StellarBurgersAPI.create_user(email, password, name)
        assert signup_response_two.status_code == 403
        assert signup_response_two.json()['success'] == False
        assert signup_response_two.json()['message'] == Message.MESSAGE_MISSING_FIELD_SIGNUP
