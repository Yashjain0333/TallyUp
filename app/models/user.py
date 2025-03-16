from typing import Optional, Any

from beanie import Document
from pydantic import BaseModel, Field

class User(Document):
    id: str = Field(None, alias="_id")
    email: str = Field(..., example="")
    password: str = Field(..., example="")
    first_name: str = Field(..., example="")
    last_name: str = Field(..., example="")
    phone_number: str = Field(..., example="")
    is_active: bool = Field(True, example=True)
    is_admin: bool = Field(False, example=False)
    is_verified: bool = Field(False, example=False)
    is_deleted: bool = Field(False, example=False)
    created_at: Optional[str] = Field(None, example="2021-09-20T00:00:00.000Z")
    last_login: Optional[str] = Field(None, example="2021-09-20T00:00:00.000Z")
    updated_at: Optional[str] = Field(None, example="2021-09-20T00:00:00.000Z")
    deleted_at: Optional[str] = Field(None, example="2021-09-20T00:00:00.000Z")

    class Config:
        json_schema_extra = {
            "example": {
                "email": "",
                "password": "password",
                "first_name": "John",
                "last_name": "Doe",
                "phone_number": "1234567890",
                "is_active": True,
            }
        }

    class Settings:
        name = "user"
        collection = "users"
        indexes = ["id", "email", "phone_number"]