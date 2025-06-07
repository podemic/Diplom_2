import allure

from src.constants import Message
from src.helpers import register_new_courier_and_return_response, context
from src.stellar_burgers_api import StellarBurgersAPI


class TestGetUserOrders:
    @allure.title('Успешный запрос получения заказов возвращает код ответа 200 и orders: []')
    def test_get_orders_with_authorization(self, delete_user_after_create):
        register_new_courier_and_return_response()
        signin_response = StellarBurgersAPI.login_user(context.get('email'), context.get('password'))
        token = signin_response.json()['accessToken']
        get_orders_response = StellarBurgersAPI.get_user_orders(token)
        assert get_orders_response.status_code == 200
        assert 'orders' in get_orders_response.json()

    @allure.title('Запрос получения заказов без авторизации возвращает код ответа 401 и message: '
                  'You should be authorised')
    def test_get_orders_without_authorization(self):
        token = None
        get_orders_response = StellarBurgersAPI.get_user_orders(token)
        assert get_orders_response.status_code == 401
        assert get_orders_response.json()["message"] == Message.MESSAGE_WITHOUT_LOGIN
