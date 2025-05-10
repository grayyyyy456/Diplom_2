import pytest
from helpers import register_new_user_and_return_login_password
from api_methods import ApiMethodsUser


@pytest.fixture
def user():
    data_create_user = register_new_user_and_return_login_password()
    ApiMethodsUser.create_user(data_create_user)

    login_data = {
        "email": data_create_user["email"],
        "password": data_create_user["password"]
    }
    response = ApiMethodsUser.login_user(login_data)
    response_data = response.json()

    access_token = response_data.get("accessToken")
    token = access_token.split(" ")[1] if access_token else None

    yield data_create_user, token

    ApiMethodsUser.delete_user(token)
