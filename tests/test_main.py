from fastapi import status

from tests.utils.client import client

def test_healthz():
    response = client.get('/healthz')

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "Up and running"}