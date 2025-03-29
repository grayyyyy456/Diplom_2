import allure
from api_methods import ApiMethodsUser
from data import ResponseTextCreateUser, DataUser


@allure.feature("Регистрация пользователей")
@allure.tag("API", "User")
class TestCreateUser:

    @allure.story("Создание нового пользователя")
    @allure.title("Проверка на создание пользователя")
    def test_create_user(self, user):
        user_data, _ = user
        assert user_data is not None
        assert 'email' in user_data
        assert 'password' in user_data
        assert 'name' in user_data

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
