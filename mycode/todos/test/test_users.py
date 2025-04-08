from .utils import *
from ..routers.users import get_current_user, get_db
from fastapi import status

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_return_user(test_user):
    response = client.get('/user')
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == 'codingwithrobytest'


def test_change_password_success(test_user):
    response = client.put('/user/password',
                          json={
                              'password': 'testpassword',
                              'new_password': 'newpassword1234'
                          })
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_change_password_invalid_nonsuccess(test_user):
    response = client.put('/user/password',
                          json={
                              'password': 'testpassword1',
                              'new_password': 'newpassword1234'
                          })
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_change_phone_success(test_user):
    response = client.put('/user/phonenumber/2222222222')
    assert response.status_code == status.HTTP_204_NO_CONTENT
