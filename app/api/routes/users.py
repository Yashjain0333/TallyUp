from fastapi import APIRouter, status
from schemas.user import User, UserCreate, UserBase
from typing import List

user_router = APIRouter()


@user_router.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    """_summary_

    Args:
        user (UserCreate): _description_
    """
    # GO TO USER SERVICE

    # Check if user already exists

    # Create user document

    # Convert ObjectId to string for the response

    # return created_user
    pass


@user_router.get("/users/", response_model=List[User])
async def get_users():
    """_summary_

    Returns:
        _type_: _description_
    """
    # GO TO USER SERVICE

    # Some Logic
    # return users
    pass
