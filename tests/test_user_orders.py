import allure
from api_methods import ApiMethodsUser
from helpers import token_get
from data import ResponseTextUserOrders

@allure.feature("Заказы пользователя")
@allure.tag("API", "User Orders")
class TestUserOrders:

    @allure.story("Получение заказа авторизованным пользователем")
    @allure.title("Проверка на получение заказа авторизированным пользователем")
    def test_get_orders_login_user(self, user):
        user_data, token = user
        ingredients_response = ApiMethodsUser.list_ingredients()
        ingredients_data = ingredients_response.json()
        ingredient_ids = [ingredients_data["data"][13]["_id"]]
        order_data = {"ingredients": ingredient_ids}
        new_token = token_get(user_data)
        ApiMethodsUser.create_order_login(new_token, order_data)
        response = ApiMethodsUser.user_login_orders(new_token)
        response_data = response.json()
        assert response.status_code == 200
        assert "orders" in response_data
        assert len(response_data["orders"]) > 0

    @allure.story("Получение заказа не авторизованным пользователем")
    @allure.title("Проверка на получение заказа не авторизированным пользователем")
    def test_get_orders_without_login_user(self):
        ingredients_response = ApiMethodsUser.list_ingredients()
        ingredients_data = ingredients_response.json()
        ingredient_ids = [ingredients_data["data"][13]["_id"]]
        order_data = {"ingredients": ingredient_ids}
        ApiMethodsUser.create_order(order_data)
        response = ApiMethodsUser.user_without_login_orders()
        assert response.status_code == 401
        assert response.json() == ResponseTextUserOrders.text_status_code_401



