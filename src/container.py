from typing import Annotated
from fastapi import Depends

from src.commands.get_user_by_id_command import GetUserByIdCommand

from src.repositories.user_repository import UserRepository

# repository
users_repository = Annotated[UserRepository, Depends(UserRepository)]

# commands
get_user_by_id_command = Annotated[GetUserByIdCommand, Depends(GetUserByIdCommand)]