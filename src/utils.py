# utils.py

from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt

# For password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Secret key for JWT (Keep this safe & private!)
SECRET_KEY = "your_secret_key_here"  # change this to a long random string
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# --------------- PASSWORD HASHING ---------------


def hash_password(password: str) -> str:
    """Hash a plain text password."""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against its hash."""
    return pwd_context.verify(plain_password, hashed_password)


# --------------- JWT TOKEN CREATION ---------------


def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    """
    Create a JWT access token.
    data: dictionary to store in token (e.g., {"sub": user_email})
    expires_delta: timedelta for expiration
    """
    to_encode = data.copy()

    expire = datetime.utcnow() + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# --------------- JWT TOKEN VERIFICATION ---------------


def verify_access_token(token: str) -> dict:
    """
    Verify the JWT token and return the payload if valid.
    Raises JWTError if invalid or expired.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
