import httpx
from jsonschema import validate
from core.contracts import USER_DATA_SCHEMA2

BASE_URL = "https://reqres.in"
LIST_RESOURCE = "/api/unknown"
SINGLE_RESOURCE = "/api/unknown/2"
NOT_FOUND_SINGLE = "/api/unknown/23"
COLOR = '#'

def test_list_resource():
    response = httpx.get(BASE_URL + LIST_RESOURCE)
    assert response.status_code == 200
    data = response.json()['data']

    for item in data:
        validate(item, USER_DATA_SCHEMA2)
        assert item['color'].startswith(COLOR)
        #     assert item['avatar'].endswith(str(item['id']) + AVATAR_ENDS)

def test_single_resource():
            response = httpx.get(BASE_URL + SINGLE_RESOURCE)
            assert response.status_code == 200
            data = response.json()['data']

            assert data['color'].startswith(COLOR)
            # assert data['avatar'].endswith(str(data['id']) + AVATAR_ENDS)

def test_single_not_found():
            response = httpx.get(BASE_URL + NOT_FOUND_SINGLE)
            assert response.status_code == 404