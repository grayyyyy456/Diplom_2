import random
import string
from api_methods import ApiMethodsUser


def register_new_user_and_return_login_password():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    email = f'{generate_random_string(10)}@yandex.ru'
    password = generate_random_string(10)
    name = generate_random_string(10)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    return payload

def token_get(user_data):
    login_response = ApiMethodsUser.login_user(user_data)
    auth_data = login_response.json()
    new_token = auth_data.get("accessToken")
    return new_token