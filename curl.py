main_site = 'https://stellarburgers.nomoreparties.site/'   # главная страница
creating_user = main_site + 'api/auth/register'  # POST создание пользователя
delete_user = main_site + 'api/auth/user'   # DELETE удаление пользователя
regist_user = main_site + 'api/auth/login'   # POST авторизация пользователя
change_data =  delete_user  #  PATCH изменение данных пользователя
ingredients = main_site + 'api/ingredients'  # GET получение списка ингредиентов
create_order = main_site + 'api/orders'  # POST создание заказа
user_orders = create_order  # GET получение заказов пользователя