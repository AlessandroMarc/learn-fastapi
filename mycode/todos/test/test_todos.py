from todos.routers.todos import get_current_user, get_db
from fastapi import status
from ..models import Todos
import pytest
from .utils import *

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


@pytest.fixture
def test_todo():
    todo = Todos(
        title="Learn to code!",
        description="Need to learn everyday!",
        priority=5,
        complete=False,
        owner_id=1,
    )

    db = TestingSessionLocal()
    db.add(todo)
    db.commit()
    yield todo
    with engine.connect() as connection:
        connection.execute(text('DELETE FROM todos'))
        connection.commit()


def test_read_all_authenticated(test_todo):
    response = client.get('/')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{
        "title": "Learn to code!",
        "description": "Need to learn everyday!",
        "priority": 5,
        "complete": False,
        "owner_id": 1,
        'id': 1
    }]


def test_read_one_authenticated(test_todo):
    response = client.get('/todo/1')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "title": "Learn to code!",
        "description": "Need to learn everyday!",
        "priority": 5,
        "complete": False,
        "owner_id": 1,
        'id': 1
    }


def test_read_one_authenticated_not_found(test_todo):
    response = client.get('/todo/1000')
    assert response.status_code == 404


def test_create_todo(test_todo):
    request_data = {
        "title": "Read a book",
        "description": "Finish reading 'Clean Code'",
        "priority": 3,
        "complete": False,
        "owner_id": 2,
        "id": 2
    }

    response = client.post('/todo/', json=request_data)
    assert response.status_code == 201

    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 2).first()
    assert model.title == request_data.get("title")


def test_update_todo(test_todo):
    request_data = {
        "title": "Learn to code!",
        "description": "Need to learn everyday!",
        "priority": 4,
        "complete": False,
        "owner_id": 1,
        'id': 1
    }

    response = client.put('/todo/1', json=request_data)
    assert response.status_code == 204
    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 1).first()
    assert model.priority == 4


def test_update_todo_not_found(test_todo):
    request_data = {
        "title": "Learn to code!",
        "description": "Need to learn everyday!",
        "priority": 4,
        "complete": False,
        "owner_id": 1,
        'id': 1
    }

    response = client.put('/todo/1000', json=request_data)
    assert response.status_code == 404
    assert response.json() == {'detail': 'Todo not found.'}


def test_delete_todo(test_todo):
    response = client.delete('/todo/1')
    assert response.status_code == 204
    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 1).first()
    assert model is None


def test_delete_todo_not_found(test_todo):
    response = client.delete('/todo/1000')
    assert response.status_code == 404
    assert response.json() == {'detail': 'Todo not found.'}
