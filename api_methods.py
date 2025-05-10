import requests
from curl import creating_user, delete_user, regist_user, change_data, ingredients, create_order, user_orders
import allure

class ApiMethodsUser:
    @staticmethod
    @allure.step("Создание пользователя")
    def create_user(data_create_user):
        return requests.post(creating_user, json=data_create_user)

    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(token):
        headers = {
            'Authorization': token
        }
        return requests.delete(delete_user, headers=headers)

    @staticmethod
    @allure.step("Создание пользователя без email")
    def create_user_without_email(data_without_login):
        return requests.post(creating_user, json=data_without_login)

    @staticmethod
    @allure.step("Создание пользователя без пароля")
    def create_user_without_password(data_without_password):
        return requests.post(creating_user, json=data_without_password)

    @staticmethod
    @allure.step("Авторизация пользователя")
    def login_user(data_login):
        return requests.post(regist_user, json=data_login)

    @staticmethod
    @allure.step("Изменение данных пользователя")
    def change_data(token, data_change):
        headers = {
            'Authorization': token
        }
        return requests.patch(change_data, headers=headers, json=data_change)

    @staticmethod
    @allure.step("Получение списка ингредиентов")
    def list_ingredients():
        return requests.get(ingredients)

    @staticmethod
    @allure.step("Создание заказа")
    def create_order(data_ingredients):
        return requests.post(create_order, json=data_ingredients)

    @staticmethod
    @allure.step("Создание заказа с авторизацией")
    def create_order_login(token, data_ingredients):
        headers = {
            'Authorization': token
        }
        return requests.post(create_order, headers=headers, json=data_ingredients)

    @staticmethod
    @allure.step("Получение заказов авторизованного пользователя")
    def user_login_orders(token):
        headers = {
            'Authorization': token
        }
        return requests.get(user_orders, headers=headers)

    @staticmethod
    @allure.step("Получение заказов без авторизации")
    def user_without_login_orders():
        return requests.get(user_orders)