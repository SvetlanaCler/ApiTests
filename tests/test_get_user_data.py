import httpx
from jsonschema import validate
from core.contracts import USER_DATA_SCHEMA
import allure

BASE_URL = "https://reqres.in"
LIST_USERS = "/api/users?page=2"
SINGLE_USER = "/api/users/2"
NOT_FOUND_USER = "/api/users/23"
EMAIL_ENDS = "@reqres.in"
AVATAR_ENDS = "-image.jpg"

@allure.suite('Проверка запросов данных пользователей')
@allure.title('Проверяем получение списка пользователей')
def test_list_users():
    with allure.step(f'Делаем запрос по адресу: {BASE_URL + LIST_USERS}'):
        response = httpx.get(BASE_URL + LIST_USERS)

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    data = response.json()['data']

    for item in data:
        with allure.step(f'Проверяем элемент из спика'):
           validate(item, USER_DATA_SCHEMA)
           with allure.step('Проверяем окончание email адреса'):
               assert item['email'].endswith(EMAIL_ENDS)
           with allure.step('Проверяем наличие id в ссылке на аватарку'):
               assert item['avatar'].endswith(str(item['id']) + AVATAR_ENDS)

def test_single_user():
            response = httpx.get(BASE_URL + SINGLE_USER)
            assert response.status_code == 200
            data = response.json()['data']

            assert data['email'].endswith(EMAIL_ENDS)
            assert data['avatar'].endswith(str(data['id']) + AVATAR_ENDS)

def test_user_not_found():
            response = httpx.get(BASE_URL + NOT_FOUND_USER)
            assert response.status_code == 404


