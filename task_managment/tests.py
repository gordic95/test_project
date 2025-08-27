import pytest
import requests


@pytest.fixture(scope="module")
def base_url():
    url = "http://localhost:8000/tasks"
    return url

@pytest.fixture(scope="module")
def task_data():
    return {
        "title": "New Task",
        "description": "This is a new task"
    }


def test_full_crud_task(base_url, task_data):
    #тесты на создание задачи
    url_create_task = f'{base_url}/create_task'
    response = requests.post(url_create_task, json=task_data)

    assert response.status_code == 201, f"Тест не пройден, задача не создана. Ответ: {response.status_code}"
    assert response.json()["title"] == task_data["title"], f"Тест не пройден, название задачи не совпадает. Ответ: {response.json()}"
    assert response.json()["description"] == task_data["description"], f"Тест не пройден, описание задачи не совпадает. Ответ: {response.json()}"

    #тесты на получения списка задач
    id_task = response.json()["id"]


    url_get_list_tasks = f'{base_url}/get_list'
    response_get_list_tasks = requests.get(url_get_list_tasks)
    if response_get_list_tasks.status_code == 200:
        for task in response_get_list_tasks.json():
            if task["id"] == id_task:
                assert response.status_code == 200, f"Тест не пройден, задачи не найдены. Ответ: {response.status_code}"
                assert task["id"] == id_task, f"Тест не пройден, id задачи не совпадает. Ответ: {response.json()}"
                assert task["title"] == task_data["title"], f"Тест не пройден, название задачи не совпадает. Ответ: {response.json()}"
                assert task["description"] == task_data["description"], f"Тест не пройден, описание задачи не совпадает. Ответ: {response.json()}"


    #тесты на получение задачи по id
    url_get_task_id = f'{base_url}/get_task/{id_task}'
    response_get_task_id = requests.get(url_get_task_id)
    if response_get_task_id.status_code == 200:
        if response_get_task_id.json()["id"] == id_task:
            assert response.status_code == 200, f"Тест не пройден, задача не найдена. Ответ: {response_get_task_id.status_code}"
            assert response_get_task_id.json()["id"] == id_task, f"Тест не пройден, id задачи не совпадает. Ответ: {response_get_task_id.json()}"
            assert response_get_task_id.json()["title"] == task_data["title"], f"Тест не пройден, название задачи не совпадает. Ответ: {response_get_task_id.json()}"
            assert response_get_task_id.json()["description"] == task_data["description"], f"Тест не пройден, описание задачи не совпадает. Ответ: {response_get_task_id.json()}"


    #тесты на редактирование задачи по id
    url_edit_task_id = f'{base_url}/update_task/{id_task}'
    response_edit_task_id = requests.put(url_edit_task_id, json={"title": "New Task", "description": "This is a new task", "status": "complete"})
    if response_edit_task_id.status_code == 200:
        if response_edit_task_id.json()["id"] == id_task:
            assert response.status_code == 200, f"Тест не пройден, задача не найдена. Ответ: {response_edit_task_id.status_code}"
            assert response_edit_task_id.json()["id"] == id_task, f"Тест не пройден, id задачи не совпадает. Ответ: {response_edit_task_id.json()}"
            assert response_edit_task_id.json()["title"] == "New Task", f"Тест не пройден, название задачи не совпадает. Ответ: {response_edit_task_id.json()}"
            assert response_edit_task_id.json()["description"] == "This is a new task", f"Тест не пройден, описание задачи не совпадает. Ответ: {response_edit_task_id.json()}"
            assert response_edit_task_id.json()["status"] == "complete", f"Тест не пройден, статус задачи не совпадает. Ответ: {response_edit_task_id.json()}"


    #тесты на удаление задачи по id
    url_delete_task_id = f'{base_url}/delete_task/{id_task}'
    response_delete_task_id = requests.delete(url_delete_task_id)
    if response_delete_task_id.status_code == 200:
        assert response.status_code == 200, f"Тест не пройден, задача не удалена. Ответ: {response_delete_task_id.status_code}"






