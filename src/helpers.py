import requests
import random
import string

from src.constants import Url

context = {}

# метод регистрации нового пользователя возвращает ответ запроса
def register_new_courier_and_return_response():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # генерируем емейл, пароль и имя пользователя
    email = f'{generate_random_string(8)}@gmail.com'
    password = generate_random_string(10)
    name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    # отправляем запрос на регистрацию пользователя
    response = requests.post(f'{Url.BASE_URL}/auth/register', json=payload)

    if response.status_code == 200:
        context['email'] = email
        context['password'] = password
        context['name'] = name

    # возвращаем ответ
    return response
