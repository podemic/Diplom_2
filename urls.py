class Urls:
    main_url = 'https://stellarburgers.nomoreparties.site'
    user_register = f'{main_url}/api/auth/register'
    user_auth = f'{main_url}/api/auth/login'
    user_update = f'{main_url}/api/auth/user'
    user_delete = f'{main_url}/api/auth/user'
    order_create = f'{main_url}/api/orders'
    get_user_orders = f'{main_url}/api/orders'

    headers = {'Content-Type': 'application/json'}