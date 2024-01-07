from fastapi import APIRouter
from fastapi_training.Handlers import user_handler, authenciate
from fastapi_training.model.user_model import User, ShowUser, Login
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/user",
    tags=['User']
)


@router.post("/register")
def register_user(user: User):
    return user_handler.register_user(user)


@router.get("/get/{email}")
def get_user(email: str) -> ShowUser:
    return user_handler.get_user(email)


@router.post("/login")
def login_user(request: OAuth2PasswordRequestForm = Depends()):
    return authenciate.login_user(request)