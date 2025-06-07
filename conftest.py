import allure
import pytest

from src.helpers import context
from src.stellar_burgers_api import StellarBurgersAPI

@pytest.fixture
@allure.step('Удаление тестовых данных после создания пользователя')
def delete_user_after_create():
    yield
    email = context.get('email')
    password = context.get('password')
    name = context.get('name')
    delete_response = StellarBurgersAPI.delete_user(email, password, name)
    assert delete_response.status_code == 200