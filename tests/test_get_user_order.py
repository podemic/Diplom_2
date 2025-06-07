from conftest import *
import requests


class TestGetOrders:
    @allure.title('Проверка успешного получения списка заказов для аутентифицированного пользователя')
    @allure.description('Аккаунт и заказ создаются фикстурой перед выполнением кода, затем тест получает '
                        'список с заказом.')
    def test_get_orders_authenticated_user_success(self, create_user_and_order_and_delete):
        headers = {'Authorization': create_user_and_order_and_delete[0]}
        response = requests.get(Urls.get_user_orders, headers=headers)
        json_response = response.json()
        assert response.status_code == 200
        assert json_response['success'] is True
        assert 'orders' in json_response.keys()
        assert 'total' in json_response.keys()

    @allure.title('Проверка ответа при запросе на получение списка заказов неаутентифицированного пользователя')
    def test_get_orders_unauthenticated_user_success(self):
        response = requests.get(Urls.get_user_orders, headers=Urls.headers)
        assert response.status_code == 401 and response.json() == {'success': False,
                                                                   'message': 'You should be authorised'}