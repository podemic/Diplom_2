from conftest import *


class TestAuthentication:
    @allure.title('Проверка логина под существующим пользователем')
    @allure.description('В post-запросе передаем креды существующего юзера, проверяем код ответа, токены')
    def test_auth_existing_account_success(self, create_new_user_and_delete):
        payload = create_new_user_and_delete[0]
        response = requests.post(Urls.user_auth, data=payload)
        json_response = response.json()
        assert response.status_code == 200
        assert json_response['success'] is True
        assert 'accessToken' in json_response.keys()
        assert 'refreshToken' in json_response.keys()
        assert json_response['user']['email'] == create_new_user_and_delete[0]['email']
        assert json_response['user']['name'] == create_new_user_and_delete[0]['name']

    @allure.title('Проверка ответа на запрос аутентификации с незарегистрированным email')
    def test_auth_with_wrong_login_expected_error(self):
        payload = {
            'email': create_random_email(),
            'password': UsersData.password,
        }
        response = requests.post(Urls.user_auth, data=payload)
        assert response.status_code == 401 and response.json() == {"success": False,
                                                                   "message": "email or password are incorrect"}

    @allure.title('Проверка ответа на запрос аутентификации с неверным паролем')
    def test_auth_with_wrong_passwd_expected_error(self):
        payload = {
            'email': UsersData.email,
            'password': create_random_password(),
        }
        response = requests.post(Urls.user_auth, data=payload)
        assert response.status_code == 401 and response.json() == {"success": False,
                                                                   "message": "email or password are incorrect"}