from .utils import *
from ..routers.auth import authenticate_user, get_db, create_access_token, SECRET_KEY, ALGORITHM, get_current_user
from jose import jwt
from datetime import timedelta
import pytest
from fastapi import HTTPException

app.dependency_overrides[get_db] = override_get_db
# app.dependency_overrides[get_current_user] = override_get_current_user


def test_authenticate_user(test_user):
    db = TestingSessionLocal()
    authenticated_user = authenticate_user(test_user.username, 'testpassword',
                                           db)
    assert authenticated_user is not None
    assert authenticated_user.username == test_user.username

    non_existent_user = authenticate_user('wrongusername', 'l', db)
    assert non_existent_user is False


def test_create_access_token():
    username = 'testuser'
    user_id = 1
    role = 'user'
    expires_delta = timedelta(days=1)

    token = create_access_token(username, user_id, role, expires_delta)

    decoded_token = jwt.decode(token,
                               SECRET_KEY,
                               algorithms=[ALGORITHM],
                               options={'verify_signature': False})

    assert decoded_token['sub'] == username


@pytest.mark.asyncio
async def test_get_current_user_valid_token():
    expected_result = {'sub': 'test_user', 'id': 1, 'user_role': 'admin'}
    encode = expected_result
    token = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

    user = await get_current_user(token)
    assert user['username'] == 'test_user'


@pytest.mark.asyncio
async def test_get_current_user_valid_token():
    expected_result = {'sub': 'test_user', 'id': 1, 'user_role': 'admin'}
    encode = expected_result
    token = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

    user = await get_current_user(token)
    assert user['username'] == 'test_user'


@pytest.mark.asyncio
async def test_missing_get_current_user():

    encode = {'role': 'user'}
    token = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

    with pytest.raises(HTTPException) as excinfo:
        await get_current_user(token=token)

    assert excinfo.value.status_code == 401
    assert excinfo.value.detail == 'Could not validate user'
