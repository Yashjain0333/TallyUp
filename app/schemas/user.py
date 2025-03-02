from pydantic import BaseModel

# User schemas
class UserBase(BaseModel):
    email: str
    name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: str

    class Config:
        orm_mode = True