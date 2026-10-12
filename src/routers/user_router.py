from fastapi import APIRouter, HTTPException, status

from src.containers.commands import get_user_by_id_command, create_user_command
from src.entitites.user_entity import UserEntity
from src.requests.create_user_request import CreateUserRequest

router = APIRouter(
    prefix='/users',
    tags=['users'],
)

@router.get('/{user_id}')
async def get_user_by_id(command: get_user_by_id_command, user_id: int):
    user = command.execute(user_id)

    if user is None:
        raise HTTPException(status_code=404, detail='User not found')

    return user

@router.post('', status_code=status.HTTP_201_CREATED)
async def create_user(command: create_user_command, request: CreateUserRequest):
    command.execute(UserEntity(**request.model_dump()))

    return {}