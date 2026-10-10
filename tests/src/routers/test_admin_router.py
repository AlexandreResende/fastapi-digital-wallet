from fastapi import status

from main import app
from src.database import get_db

from tests.utils.database import override_get_db
from tests.utils.client import client
from tests.utils.fixtures.repositories.users_repository.user_repository_fixture import user

app.dependency_overrides[get_db] = override_get_db

def test_admin_get_user_by_id(user):
    response = client.get('/admin/users/1')

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        'id': 1, 'username': 'username', 'password': 'password', 'email': 'test@gmail.com', 'is_active': True, 'role': 'admin', 'first_name': 'Tester', 'last_name': 'Testing'
    }

def test_admin_get_user_by_id_not_found():
    response = client.get('/admin/users/2')

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'User not found'}

def test_admin_update_user_by_id(user):
    response = client.put('/admin/users/1', json={ 'username': 'Testonildo' })

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == { 'message': 'User updated successfully' }

def test_admin_update_user_by_id_with_invalid_data(user):
    response = client.put('/admin/users/1', json={ 'username': 'T' })

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT
