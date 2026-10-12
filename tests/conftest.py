import pytest

from main import app
from src.database import Base, get_db
from tests.utils.database import engine, override_get_db

@pytest.fixture(autouse=True)
def clean_database():
    app.dependency_overrides[get_db] = override_get_db
    Base.metadata.create_all(bind=engine)

    yield

    Base.metadata.drop_all(bind=engine)
    app.dependency_overrides.clear()
