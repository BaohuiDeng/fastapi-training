from fastapi_training.Handlers.authenciate import get_password_hash
from fastapi_training.model.user_model import User
from fastapi_training.database import fastapi_training
from fastapi import HTTPException, status



def register_user(user:User, status_code=201):
    found_user = fastapi_training.user.find_one({'email': user.email})
    if found_user:
        status_code = status.HTTP_400_BAD_REQUEST
        return {'error': 'Email already registered'}
    user.password =   get_password_hash(user.password)
    result = fastapi_training.user.insert_one(user.dict())
    return {'user': str(result.inserted_id)}


def get_user(email: str):
    found_user = fastapi_training.user.find_one({'email': email})
    if found_user:
        found_user['_id'] = str(found_user['_id'])
        return found_user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with email {email} not found')

