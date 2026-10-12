from src.containers.repositories import users_repository
from src.entitites.user_entity import UserEntity


class CreateUserCommand:
    def __init__(self, repository: users_repository):
        self.repository = repository

    def execute(self, user: UserEntity):
        self.repository.create_user(user)

        return