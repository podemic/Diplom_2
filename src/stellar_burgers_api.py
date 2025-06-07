import allure
import requests
from src.constants import Url


class StellarBurgersAPI:
    @staticmethod
    @allure.step('Запрос создания пользователя')
    def create_user(email, password, name):
        url = f'{Url.BASE_URL}/auth/register'
        payload = {"email": email, "password": password, "name": name}
        return requests.post(url, json=payload)

    @staticmethod
    @allure.step('Запрос удаления пользователя')
    def delete_user(email, password, name):
        url = f'{Url.BASE_URL}/auth/register'
        payload = {"email": email, "password": password, "name": name}
        return requests.delete(url, json=payload)

    @staticmethod
    @allure.step('Запрос авторизации пользователя')
    def login_user(email, password):
        url = f"{Url.BASE_URL}/auth/login"
        payload = {"email": email, "password": password}
        return requests.post(url, json=payload)

    @staticmethod
    def update_user(token, email=None, name=None):
        url = f"{Url.BASE_URL}/auth/user"
        headers = {"Authorization": token}
        payload = {"email": email, "name": name}
        return requests.patch(url, json=payload, headers=headers)

    @staticmethod
    def create_order(token, ingredients):
        url = f"{Url.BASE_URL}/orders"
        headers = {"Authorization": token}
        payload = {"ingredients": ingredients}
        return requests.post(url, json=payload, headers=headers)

    @staticmethod
    def get_user_orders(token):
        url = f"{Url.BASE_URL}/orders"
        headers = {"Authorization": token}
        return requests.get(url, headers=headers)
