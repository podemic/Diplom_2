from faker import Faker


class Url:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/api'


class Account:
    fake = Faker('ru_RU')
    USER_DATA = {
        'email': fake.unique.email(),
        'password': fake.unique.password(),
        'name': fake.unique.first_name()
    }


class Message:
    MESSAGE_EXISTING_SIGNUP = 'User already exists'
    MESSAGE_MISSING_FIELD_SIGNUP = 'Email, password and name are required fields'
    MESSAGE_INVALID_FIELD_LOGIN = 'email or password are incorrect'
    MESSAGE_WITHOUT_LOGIN = 'You should be authorised'
    MESSAGE_WITHOUT_INGREDIENT = 'Ingredient ids must be provided'
    MESSAGE_INVALID_INGREDIENT = 'One or more ids provided are incorrect'


class Ingredient:
    VALID_INGREDIENTS = ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
    INVALID_INGREDIENTS = ["invalid-hash"]
