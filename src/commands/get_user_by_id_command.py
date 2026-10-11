from fastapi.params import Depends

from src.container import users_repository


class GetUserByIdCommand:
    def __init__(self, repository: users_repository):
        self.repository = repository

    def execute(self, user_id: int):
        user = self.repository.get_user_by_id(user_id)

        if user is None:
            return None

        return user