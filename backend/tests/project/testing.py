from utils import create_team, url
import requests
from models import Project


def test_create_project():
    product, writer, head_writer, analyst = create_team()
    create_proj_data = {
        "name": 'string',
        "theme": 'string',
        "target_desc": 'string',
        "goal": 'string',
        "users": f"[{writer.id},{head_writer.id},{analyst.id}]",
    }
    headers = {"Authorization": product.session}
    response = requests.post(f"{url}/projects", params=create_proj_data, headers=headers)
    data = response.json()
    if response != 200 or None in (
            data.get('id'), data.get('name'), data.get('theme'), data.get('target_desc'), data.get('goal'),
            data.get('is_archive'), data.get('attachments'), data.get('users'), data.get('stages')):
        return 0
    return 1


def get_project() -> Project:
    product, writer, head_writer, analyst = create_team()
    create_proj_data = {
        "name": 'string',
        "theme": 'string',
        "target_desc": 'string',
        "goal": 'string',
        "users": f"[{writer.id},{head_writer.id},{analyst.id}]",
    }
    headers = {"Authorization": product.session}
    response = requests.post(f"{url}/projects", params=create_proj_data, headers=headers)
    data = response.json()
    return Project(**response.json(), session=session)


def test_get_project():
    project = get_project()
    params = {'project_id': project.id}
    response = requests.get(f"{url}/projects", params=params, headers=headers)
    data = response.json()
    if response != 200 or None in (
            data.get('id'), data.get('name'), data.get('theme'), data.get('target_desc'), data.get('goal'),
            data.get('is_archive'), data.get('attachments'), data.get('users'), data.get('stages')):
        return 0
    return 1


def test_fetch_projects():
    params = {'search': "string",
              "offset": 0,
              "limit": 1}
    response = requests.get(f"{url}/projects/fetch", params=params, headers=headers)
    data = response.json()
    if response != 200 or None in (data.get('total'), data.get('pages'), data.get('res')):
        return 0
    return 1


def test_project_by_stage():
    project = get_project()
    params = {'stage_id': 0,
              "project_id": project.id
              }
    response = requests.post(f"{url}/projects/0", params=params, headers=headers)
    data = response.json()
    if response != 200 or None in (
            data.get('id'), data.get('stage'), data.get('status'), data.get('payload'), data.get('history_payload'),
            data.get('comment')):
        return 0
    return 1


testcase = (test_create_project(), test_get_project(), test_fetch_projects(), test_project_by_stage())

summ = sum(testcase)
print(f'Тесты покрыли {summ / len(testcase) * 100}% всего функицонала этого сервиса')
