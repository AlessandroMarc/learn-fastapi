from .utils import *
from ..routers.admin import get_current_user, get_db
from fastapi import status
from ..models import Todos

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_admin_read_all_authenticated(test_todo):
    response = client.get('/admin/todo')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1


def test_admin_delete_todos(test_todo):
    response = client.delete('/admin/todo/1')
    assert response.status_code == 204
    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 1).first()
    assert model is None


def test_admin_delete_todos_not_found(test_todo):
    response = client.delete('/admin/todo/100')
    assert response.status_code == 404
