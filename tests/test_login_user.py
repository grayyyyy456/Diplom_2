import allure
from api_methods import ApiMethodsUser
from data import ResponseTextLoginUser, DataUser


@allure.feature("Авторизация пользователя")
@allure.tag("API", "User Login")
class TestLoginUser:

    @allure.story("Авторизация с корректными данными")
    @allure.title("Проверка что существующий пользователь может авторизороваться")
    def test_user_authorization(self):
        data_login = {
            'email': DataUser.email,
            'password': DataUser.password
        }
        response = ApiMethodsUser.login_user(data_login)
        request = response.json()
        assert response.status_code == 200
        assert request['success'] is True
        assert request['accessToken'].startswith("Bearer ")
        assert request['user']['email'] == DataUser.email
        assert request['user']['name'] == DataUser.name

    @allure.story("Авторизация с некорректным паролем")
    @allure.title("Проверка что несуществующий пользователь с некорректным паролем не может авторизороваться")
    def test_user_authorization_with_wrong_password(self):
        data_login = {
            'email': DataUser.email,
            'password': DataUser.password+'a'
        }
        response = ApiMethodsUser.login_user(data_login)
        assert response.status_code == 401
        assert ResponseTextLoginUser.text_status_code_401 == response.json()

    @allure.story("Авторизация с некорректным email")
    @allure.title("Проверка что несуществующий пользователь с некорректным email не может авторизороваться")
    def test_user_authorization_with_wrong_email(self):
        data_login = {
            'email': DataUser.email+'a',
            'password': DataUser.password
        }
        response = ApiMethodsUser.login_user(data_login)
        assert response.status_code == 401
        assert ResponseTextLoginUser.text_status_code_401 == response.json()
