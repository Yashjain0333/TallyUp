import secrets
import string
from datetime import datetime, timedelta, timezone
from typing import Optional, Dict, Any
from passlib.context import CryptContext
import jwt
from jwt.exceptions import InvalidTokenError

from config.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    """
    Hash a password using bcrypt algorithm
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a password against its hash
    """
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Create a JWT access token
    """
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


def create_refresh_token(data: dict) -> str:
    """
    Create a JWT refresh token with longer expiration
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )
    to_encode.update({"exp": expire, "type": "refresh"})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


def generate_reset_token(length: int = 32) -> str:
    """
    Generate a secure random token for password reset
    """
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))


def decode_token(token: str) -> Dict[str, Any]:
    """
    Decode a JWT token and return its payload
    """
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        return payload
    except InvalidTokenError:
        return {}


def is_token_valid(token: str, token_type: str = "access") -> tuple:
    """
    Check if a token is valid and of the correct type
    """
    payload = decode_token(token)
    if not payload:
        return False

    if "type" not in payload or payload["type"] != token_type:
        return False

    # Check if token has expired
    if "exp" not in payload:
        return False

    expiration = datetime.fromtimestamp(payload["exp"])
    if expiration < datetime.now(timezone.utc):
        return False

    return (True, payload)
