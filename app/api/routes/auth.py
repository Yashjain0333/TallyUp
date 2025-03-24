"""Authentication Router"""

from datetime import timedelta
from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError

from schemas._user import User, UserCreate
from schemas._auth import Token, TokenData
from utils.encryption_utils import create_access_token, is_token_valid

from config.config import settings

auth_router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")
credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

#! Remove this
user = User(
    **{
        "email": "abc@gmail.com",
        "password": "password",
        "name": "John Doe",
        # "last_name": "Doe",
        "phone_number": "1234567890",
        "is_active": True,
    }
)

@auth_router.post("/signup", response_model=User)
async def signup_user(user_data: UserCreate):
    try:
        ## FOR Vinayak : Check if user already exists
        # This would be implemented with your database
        # existing_user = get_user_by_email(user_data.email)
        # if existing_user:
        #     raise HTTPException(
        #         status_code=status.HTTP_400_BAD_REQUEST,
        #         detail="User with this email already exists",
        #     )
        
        # Hash the password before storing
        # user_data.password = get_password_hash(user_data.password)
        
        # Store the user in the database
        # new_user = create_user_in_db(user_data)
        
        # For now, just return the user data without the password
        # In a real implementation, you would return the new_user from the database
        user_response = User(
            email=user_data.email,
            name=user_data.name,
            # phone_number=user_data.phone_number,
            is_active=True,
        )
        
        return user_response
        
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error creating user. Please contact admin.",
        ) from e

@auth_router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    try:
        ## FOR Vinayak : Implement Add User to DB Here
        # user = authenticate_user(fake_users_db, form_data.username, form_data.password)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(
            minutes=int(settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        access_token = create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )
        return Token(access_token=access_token, token_type="bearer")
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Please Contact Admin",
        ) from e


@auth_router.get("/users/me/")
async def get_current_user(token: Annotated[User, Depends(oauth2_scheme)]):
    try:
        _itv, payload = is_token_valid(token)
        if not _itv:
            raise credentials_exception
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)

        ## FOR Vinayak : Implement Get User from DB Here
        # user = get_user(fake_users_db, username=token_data.username)
        # if user is None:
        #     raise credentials_exception
        # if not user.is_active:
        #     raise HTTPException(status_code=400, detail="Inactive user")

        # return user
        return token_data  ## this is garbage return

    except InvalidTokenError as e:
        raise credentials_exception from e


# async def read_users_me(
#     current_user: Annotated[User, Depends(get_current_user)],
# ):
#     return current_user
