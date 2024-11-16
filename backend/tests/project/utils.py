import requests
from models import User
from random import choices
import string

url = 'http://127.0.0.1:8000'


def generate_email():
    return f"{''.join(choices(string.ascii_letters, k=10))}@mail.ru"


def create_product() -> User:
    data = {
        "name": "Андрей Иванов",
        "email": generate_email(),
        "role": 0,
        "password": "string"
    }
    response = requests.post(f'{url}/users', json=data)
    session = response.json().get('session')
    response = requests.get(f'{url}/users', headers={"Authorization": session})
    return User(**response.json(), session=session)


def create_writer() -> User:
    data = {
        "name": "Андрей Иванов",
        "email": generate_email(),
        "role": 1,
        "password": "string"
    }
    response = requests.post(f'{url}/users', json=data)
    session = response.json().get('session')
    response = requests.get(f'{url}/users', headers={"Authorization": session})
    return User(**response.json(), session=session)


def create_head_writer() -> User:
    data = {
        "name": "Андрей Иванов",
        "email": generate_email(),
        "role": 2,
        "password": "string"
    }
    response = requests.post(f'{url}/users', json=data)
    session = response.json().get('session')
    response = requests.get(f'{url}/users', headers={"Authorization": session})
    return User(**response.json(), session=session)


def create_analyst() -> User:
    data = {
        "name": "Андрей Иванов",
        "email": generate_email(),
        "role": 3,
        "password": "string"
    }
    response = requests.post(f'{url}/users', json=data)
    session = response.json().get('session')
    response = requests.get(f'{url}/users', headers={"Authorization": session})
    return User(**response.json(), session=session)


def create_team() -> tuple[User]:
    product = create_product()
    writer = create_writer()
    head_writer = create_head_writer()
    analyst = create_analyst()
    return product, writer, head_writer, analyst