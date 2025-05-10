import allure
from api_methods import ApiMethodsUser
from data import ResponseTextChangeData
from helpers import token_get

@allure.feature("Изменение данных пользователя")
@allure.tag("API", "User Data")
class TestDataChange:

    @allure.story("Изменение имени у авторизованного пользователя")
    @allure.title("Проверка на изменении имени у авторизированного пользователя")
    def test_change_data_authorized_user(self, user):
        user_data, token = user
        new_token = token_get(user_data)
        new_name = {'user': {'name': 'serg'}}
        response = ApiMethodsUser.change_data(new_token, new_name)
        response_data = response.json()
        assert response.status_code == 200
        assert response_data["success"] is True
        assert response_data["user"]["email"] == user_data["email"]
        assert response_data["user"]["name"] == user_data["name"]

    @allure.story("Изменение email у авторизованного пользователя")
    @allure.title("Проверка на изменении email у авторизированного пользователя")
    def test_change_email_authorized_user(self, user):
        user_data, token = user
        new_token = token_get(user_data)
        new_email = {'user': {'email': 'serg123@yandex.ru'}}
        response = ApiMethodsUser.change_data(new_token, new_email)
        response_data = response.json()
        assert response.status_code == 200
        assert response_data["success"] is True
        assert response_data["user"]["email"] == user_data["email"]
        assert response_data["user"]["name"] == user_data["name"]

    @allure.story("Ошибка при изменении данных у не авторизованного пользователя")
    @allure.title("Проверка на ошибку при изменении имени у не авторизированного пользователя")
    def test_change_name_unauthorized_user(self, user):
        user_data, token = user
        new_name = {'name': 'sergio'}
        response = ApiMethodsUser.change_data(token, new_name)
        assert response.status_code == 401
        assert ResponseTextChangeData.text_status_code_401 == response.json()

    @allure.story("Ошибка при изменении данных у не авторизованного пользователя")
    @allure.title("Проверка на ошибку при изменении email у не авторизированного пользователя")
    def test_change_email_unauthorized_user(self, user):
        user_data, token = user
        new_pass = {'email': 'serg123@yandex.ru'}
        response = ApiMethodsUser.change_data(token, new_pass)
        assert response.status_code == 401
        assert ResponseTextChangeData.text_status_code_401 == response.json()
