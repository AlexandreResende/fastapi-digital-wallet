from typing import Annotated
from fastapi import Depends

from src.repositories.user_repository import UserRepository

# repository
users_repository = Annotated[UserRepository, Depends(UserRepository)]