import requests

api_url = 'https://jsonplaceholder.typicode.com/users'


def get_users():
    response = requests.get(api_url)
    return response


def test_get_users_status_code():
    response = get_users()
    assert response.status_code == 200
