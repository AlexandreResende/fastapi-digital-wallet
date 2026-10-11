from typing import Annotated
from fastapi import Depends

from src.repositories.user_repository import UserRepository

users_repository = Annotated[UserRepository, Depends(UserRepository)]