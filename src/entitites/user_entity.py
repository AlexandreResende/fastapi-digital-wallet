from typing import Optional

from src.models import Users

class UserEntity:
    id: Optional[int] = None
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    is_active: bool
    role: str

    def __init__(self, id: int, username: str, email: str, first_name: str, last_name: str, password: str, is_active: bool, role: str):
        self.id = id
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.is_active = is_active
        self.role = role

    def to_database(self):
        return Users(
            username=self.username,
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name,
            id=self.id,
            password=self.password,
            is_active=self.is_active,
            role=self.role
        )

    @staticmethod
    def from_database(id: int, username: str, email: str, first_name: str, last_name: str, password: str, is_active: bool, role: str):
        user = UserEntity(id, username, email, first_name, last_name, password, is_active, role)

        return user