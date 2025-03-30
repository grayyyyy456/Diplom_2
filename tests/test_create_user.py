import allure
from api_methods import ApiMethodsUser
from data import ResponseTextCreateUser, DataUser
from helpers import register_new_user_and_return_login_password


@allure.feature("Регистрация пользователей")
@allure.tag("API", "User")
class TestCreateUser:

    @allure.story("Создание нового пользователя")
    @allure.title("Проверка на создание пользователя")
    def test_create_user(self):
        user_data = register_new_user_and_return_login_password()
        ApiMethodsUser.create_user(user_data)
        login_data = {
            "email": user_data["email"],
            "password": user_data["password"]
        }
        response = ApiMethodsUser.login_user(login_data)
        response_data = response.json()
        access_token = response_data.get("accessToken")
        token = access_token.split(" ")[1] if access_token else None

        assert user_data is not None
        assert 'email' in user_data
        assert 'password' in user_data
        assert 'name' in user_data
        ApiMethodsUser.delete_user(token)

    @allure.story("Создание уже существующего пользователя")
    @allure.title("Проверка на ошибку, при создании уже существующего пользователя")
    def test_create_two_identical_user(self, user):
        user_data, _ = user
        response = ApiMethodsUser.create_user(user_data)
        assert response.status_code == 403
        assert ResponseTextCreateUser.text_status_code_403_two == response.json()

    @allure.story("Создание пользователя без email")
    @allure.title("Проверка на ошибку, при создании пользователя без логина")
    def test_create_user_without_email(self):
        data_without_email = {"password": DataUser.password}
        response = ApiMethodsUser.create_user_without_email(data_without_email)
        assert response.status_code == 403
        assert ResponseTextCreateUser.text_status_code_403_none == response.json()

    @allure.story("Создание пользователя без пароля")
    @allure.title("Проверка на ошибку, при создании пользователя без пароля")
    def test_create_user_without_password(self):
        data_without_password = {"login": DataUser.email}
        response = ApiMethodsUser.create_user_without_password(data_without_password)
        assert response.status_code == 403
        assert ResponseTextCreateUser.text_status_code_403_none == response.json()
