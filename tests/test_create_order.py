import allure

from src.constants import Ingredient, Message
from src.helpers import register_new_courier_and_return_response, context
from src.stellar_burgers_api import StellarBurgersAPI


class TestCreateOrder:
    @allure.title('Успешный запрос создание заказа возвращает код ответа 200 и success: True')
    def test_create_order_with_authorization_and_valid_ingredients(self, delete_user_after_create):
        register_new_courier_and_return_response()
        signin_response = StellarBurgersAPI.login_user(context.get('email'), context.get('password'))
        token = signin_response.json()['accessToken']
        create_order_response = StellarBurgersAPI.create_order(token, Ingredient.VALID_INGREDIENTS)
        assert create_order_response.status_code == 200
        assert create_order_response.json()['success'] == True

    # Данный тест не проходит. Это баг.
    @allure.title('Запрос создание заказа без авторизации возвращает код ответа 401')
    def test_create_order_without_authorization(self, delete_user_after_create):
        register_new_courier_and_return_response()
        token = None
        create_order_response = StellarBurgersAPI.create_order(token, Ingredient.VALID_INGREDIENTS)
        assert create_order_response.status_code == 401

    @allure.title('Запрос создание заказа без ингредиентов возвращает код ответа 400 и message: '
                  'Ingredient ids must be provided')
    def test_create_order_without_ingredients(self, delete_user_after_create):
        register_new_courier_and_return_response()
        signin_response = StellarBurgersAPI.login_user(context.get('email'), context.get('password'))
        token = signin_response.json()['accessToken']
        create_order_response = StellarBurgersAPI.create_order(token, '')
        assert create_order_response.status_code == 400
        assert create_order_response.json()['message'] == Message.MESSAGE_WITHOUT_INGREDIENT

    @allure.title('Запрос создание заказа с неверным хэшем ингредиентов возвращает код ответа 400 и message: '
                  'One or more ids provided are incorrect')
    def test_create_order_with_invalid_ingredients(self, delete_user_after_create):
        register_new_courier_and_return_response()
        signin_response = StellarBurgersAPI.login_user(context.get('email'), context.get('password'))
        token = signin_response.json()['accessToken']
        create_order_response = StellarBurgersAPI.create_order(token, Ingredient.INVALID_INGREDIENTS)
        assert create_order_response.status_code == 400
        assert create_order_response.json()['message'] == Message.MESSAGE_INVALID_INGREDIENT
