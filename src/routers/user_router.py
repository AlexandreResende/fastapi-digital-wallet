from fastapi import APIRouter, HTTPException

from src.containers.commands import get_user_by_id_command

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