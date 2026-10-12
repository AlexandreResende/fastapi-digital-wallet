from fastapi import status

from tests.utils.client import client
from tests.utils.fixtures.repositories.users_repository.user_repository_fixture import user

def test_get_user_by_id(user):
    response = client.get('/users/1')

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        'id': 1, 'username': 'username', 'password': 'password', 'email': 'test@gmail.com', 'is_active': True, 'role': 'admin', 'first_name': 'Tester', 'last_name': 'Testing'
    }

def test_get_user_by_username_not_found():
    response = client.get('/users/1')

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == { 'detail': 'User not found' }

def test_create_user():
    response = client.post('/users', json={
        'username': 'alexandre',
        'email': 'a2@gmail.com',
        'first_name': 'alexandre',
        'last_name': 'Doe',
        'password': '123456',
        'role': 'developer'
    })

    assert response.status_code == status.HTTP_201_CREATED

# def test_create_user_with_invalid_data():
#     response = client.post('/users', json={
#         'username': 'b',
#         'email': 'a3@gmail.com',
#         'first_name': 'alexandre',
#         'last_name': 'Doe',
#         'password': '123456',
#         'role': 'developer'
#     })
#
#     assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT