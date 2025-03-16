from typing import List, Union

from beanie import PydanticObjectId

from app.models.user import User


def check_user_is_active(user: User) -> bool:
    return user.is_active


def check_user_is_admin(user: User) -> bool:
    return user.is_admin


def check_user_is_verified(user: User) -> bool:
    return user.is_verified


def check_user_is_deleted(user: User) -> bool:
    return user.is_deleted


# not that good of a function
# async def update_user(user: User) -> User:
#     user = await user.update()
#     return user


def filter_deleted_users(users: List[User]) -> List[User]:
    return [user for user in users if not user.is_deleted]


async def create_user(new_user: User) -> User:
    user = await new_user.create()
    return user


async def get_user_by_id(user_id: PydanticObjectId) -> Union[User, None]:
    user = await User.get(user_id)
    return user


async def get_user_by_email(email: str) -> Union[User, None]:
    user = await User.get(email=email)
    return user


async def get_user_by_phone_number(phone_number: str) -> Union[User, None]:
    user = await User.get(phone_number=phone_number)
    return user


async def get_all_users() -> List[User]:
    users = await User.all().to_list()
    return users
