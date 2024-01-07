from datetime import datetime, timedelta
from http.client import HTTPException
from typing import Union
from passlib.context import CryptContext
from fastapi_training.model.user_model import Login, TokenData
from jose import JWTError, jwt
from fastapi_training.database import fastapi_training
from fastapi import HTTPException, status
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caadfee6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def login_user(request: OAuth2PasswordRequestForm = Depends()):
    found_user = fastapi_training.user.find_one({'email': request.username})
    if found_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Incorrect password with {request.username}')

    if not verify_password(request.password, found_user['password']):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f'Incorrect password with {request.username}')
    
    
    generated_token = create_access_token(data={"sub": request.username})
    return {"access_token": generated_token, "token_type": "bearer"}


def verify_token(token: str ,credentials_exception:HTTPException):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
