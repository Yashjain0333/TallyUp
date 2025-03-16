from datetime import datetime
from pydantic import BaseModel
from typing import Optional


# RefreshToken schema
class RefreshToken(BaseModel):
    refresh_token: str


# Token schemas
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    refresh_token: Optional[str] = None
    user_id: Optional[str] = None
    expires_at: Optional[datetime] = None


class TokenData(BaseModel):
    user_id: Optional[str] = None
    token_type: Optional[str] = None
