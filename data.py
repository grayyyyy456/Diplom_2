class DataUser:
    email = "gray1313@yandex.ru"
    password = "1234"
    name = "sergio"

class ResponseTextCreateUser:
    text_status_code_201 = {"ok": True}
    text_status_code_403_two = {"success": False,"message": "User already exists"}
    text_status_code_403_none = {"success": False,"message": "Email, password and name are required fields"}

class ResponseTextLoginUser:
    text_status_code_200 = {
"success": True,
"accessToken": "Bearer ...",
"refreshToken": "",
"user": {
"email": "",
"name": ""
}
}
    text_status_code_401 = {
"success": False,
"message": "email or password are incorrect"
}

class ResponseTextChangeData:
    text_status_code_401 = {
"success": False,
"message": "You should be authorised"
}

    text_status_code_403 = {
"success": False,
"message": "User with such email already exists"
}

class ResponseTextCreateOrder:
    text_status_code_400 = {
"success": False,
"message": "Ingredient ids must be provided"
}

class ResponseTextUserOrders:
    text_status_code_401 = {
"success": False,
"message": "You should be authorised"
}