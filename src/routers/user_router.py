from fastapi import APIRouter, HTTPException

from src.container import users_repository

router = APIRouter(
    prefix='/users',
    tags=['users'],
)

@router.get('/{user_id}')
async def get_user_by_id(repository: users_repository, user_id: int):
    user = repository.get_user_by_id(user_id)

    if user is None:
        raise HTTPException(status_code=404, detail='User not found')

    return user