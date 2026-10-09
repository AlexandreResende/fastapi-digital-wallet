from src.models import Users
from src.database import db_dependency

from src.entitites.user_entity import UserEntity


class UserRepository:
    def __init__(self, db: db_dependency):
        self.db = db

    def get_user_by_id(self, user_id: int):
        user = self.db.query(Users).filter(UserEntity.id == user_id).first()

        if user is None:
            return None

        return UserEntity.from_database(**user.to_json())