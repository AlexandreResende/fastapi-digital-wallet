from fastapi import APIRouter, HTTPException, status

from src.container import users_repository
from src.requests.admin_update_user import AdminUpdateUser

router = APIRouter(
    prefix='/admin',
    tags=['admin'],
)

@router.get('/users/{user_id}')
async def admin_get_user(repository: users_repository, user_id: int):
    user = repository.get_user_by_id(user_id)

    if user is None:
        raise HTTPException(status_code=404, detail='User not found')

    return user

@router.put('/users/{user_id}', status_code=status.HTTP_200_OK)
async def admin_update_user(repository: users_repository, user_id: int, request: AdminUpdateUser):
    repository.update_user_by_id(user_id, request.model_dump(exclude_unset=True))

    return {'message': 'User updated successfully'}