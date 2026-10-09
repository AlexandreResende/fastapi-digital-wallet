from fastapi import APIRouter, HTTPException

from src.container import users_repository

router = APIRouter(
    prefix='/admin',
    tags=['admin'],
)

@router.get('/users/{user_id}')
async def get_user(repository: users_repository, user_id: int):
    user = repository.get_user_by_id(user_id)

    if user is None:
        raise HTTPException(status_code=404, detail='User not found')

    return user