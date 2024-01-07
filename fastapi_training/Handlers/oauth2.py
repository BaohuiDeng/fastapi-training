from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from .authenciate import verify_token


# is the route where fast api will get the token from
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")


def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    print('data',data)
    return verify_token(data,credentials_exception)
    # user = get_user(fake_users_db, username=token_data.username)
    # if user is None:
    #     raise credentials_exception
    # return user
