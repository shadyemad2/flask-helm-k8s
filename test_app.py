import pytest
from app import app as flask_app, tasks  # Import the tasks dictionary

# Fixture to provide the app
@pytest.fixture
def app():
    yield flask_app

# Fixture to provide the test client
@pytest.fixture
def client(app):
    return app.test_client()

# Test the homepage loads successfully
def test_index(app, client):
    response = client.get('/')
    assert response.status_code == 200

# Test adding a task
def test_add_task(client):
    response = client.post('/', data={'task_content': 'New Task', 'add_task': True})
    assert response.status_code == 200
    assert 'New Task' in tasks.values()

# Test deleting a task
def test_delete_task(client):
    client.post('/', data={'task_content': 'Task to Delete', 'add_task': True})
    task_id_to_delete = list(tasks.keys())[0]
    response = client.post('/', data={'task_id_to_delete': task_id_to_delete, 'delete_task': True})
    assert response.status_code == 200
    assert task_id_to_delete not in tasks

