from typing import Annotated

from fastapi import Depends
from src.commands.get_user_by_id_command import GetUserByIdCommand

get_user_by_id_command = Annotated[GetUserByIdCommand, Depends(GetUserByIdCommand)]