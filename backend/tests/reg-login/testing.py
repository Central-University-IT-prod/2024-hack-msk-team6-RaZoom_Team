import requests
from utils import generate_email
url = 'http://127.0.0.1:8000'

email = generate_email()
password = 'parol-carol'

def test_register():
    register_data = {
        "name": "Андрей Иванов",
        "email": email,
        "role": 0,
        "password": password
    }
    response = requests.post(f'{url}/users', json=register_data)
    if response.status_code != 200 or response.json().get("session") == None:
        return 0
    return 1


def test_login():
    login_data = {
        "email": email,
        "password": password,
    }
    response = requests.post(f'{url}/auth', json=login_data)
    if response.status_code != 200 or response.json().get("session") == None:
        return 0
    return 1

def get_session(email, password):
    login_data = {
        "email": email,
        "password": password,
    }
    response = requests.post(f'{url}/auth', json=login_data)
    if response.status_code == 200 and response.json().get("session") != None:
        return response.json().get("session")

def test_userinfo():
    session = get_session(email, password)
    headers = {"Authorization": session}
    response = requests.get(f'{url}/users', headers=headers)
    data = response.json()
    if response.status_code != 200 or None in (data.get('name'), data.get('email'), data.get('role'), data.get('id'), data.get('working_projects')):
        return 0
    return 1



print(test_register())
print(test_login())
print(test_userinfo())


testcase = (test_register(), test_login(), test_userinfo())

summ = sum(testcase)
print(f'Тесты покрыли {summ/len(testcase) * 100}% всего функицонала этого сервиса')