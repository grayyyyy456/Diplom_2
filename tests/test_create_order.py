import allure
from api_methods import ApiMethodsUser
from helpers import token_get
from data import ResponseTextCreateOrder


@allure.feature("Оформление заказов")
@allure.tag("API", "Order")
class TestCreateOrder:

    @allure.story("Создание заказа без авторизации")
    @allure.title("Проверка на создание заказа без авторизации")
    def test_create_order_without_login(self):
        ingredients_response = ApiMethodsUser.list_ingredients()
        ingredients_data = ingredients_response.json()
        ingredient_ids = [ingredients_data["data"][0]["_id"], ingredients_data["data"][1]["_id"]]
        order_data = {"ingredients": ingredient_ids}
        response = ApiMethodsUser.create_order(order_data)
        response_data = response.json()
        assert response.status_code == 200
        assert response_data["success"] is True
        assert "order" in response_data
        assert "number" in response_data["order"]
        assert "price" not in response_data["order"]

    @allure.story("Создание заказа с авторизацией")
    @allure.title("Проверка на создание заказа с авторизацией")
    def test_create_order_login(self, user):
        user_data, token = user
        ingredients_response = ApiMethodsUser.list_ingredients()
        ingredients_data = ingredients_response.json()
        ingredient_ids = [ingredients_data["data"][0]["_id"], ingredients_data["data"][1]["_id"]]
        new_token = token_get(user_data)
        order_data = {"ingredients": ingredient_ids}
        response = ApiMethodsUser.create_order_login(new_token, order_data)
        response_data = response.json()
        assert response.status_code == 200
        assert response_data["success"] is True
        assert "order" in response_data
        assert "number" in response_data["order"]
        assert "price" in response_data["order"]
        assert response_data["order"]["owner"]["email"] == user_data["email"]
        assert response_data["order"]["owner"]["name"] == user_data["name"]

    @allure.story("Создание заказа без ингредиентов")
    @allure.title("Проверка на создание заказа без ингредиентов")
    def test_create_order_ingredients(self):
        order_data = {}
        response = ApiMethodsUser.create_order(order_data)
        assert response.status_code == 400
        assert response.json() == ResponseTextCreateOrder.text_status_code_400

    @allure.story("Создание заказа с невалидными ингредиентами")
    @allure.title("Проверка на создание заказа с несуществующими ингредиентами")
    def test_create_order_without_login(self):
        ingredient_ids = [123456789, 987654321]
        order_data = {"ingredients": ingredient_ids}
        response = ApiMethodsUser.create_order(order_data)
        assert response.status_code == 500
