from pytest import fixture

from src.models import Users
from tests.utils.database import TestingSessionLocal

@fixture
def user():
    user = Users(
        username='username',
        password='password',
        email='test@gmail.com',
        first_name='Tester',
        last_name='Testing',
        is_active=True,
        role='admin',
        id=1
    )

    db = TestingSessionLocal()
    db.add(user)
    db.commit()
    db.close()

    yield user
