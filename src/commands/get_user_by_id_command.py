from src.containers.repositories import users_repository

class GetUserByIdCommand:
    def __init__(self, repository: users_repository):
        self.repository = repository

    def execute(self, user_id: int):
        return self.repository.get_user_by_id(user_id)
