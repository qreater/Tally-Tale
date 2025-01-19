"""
 Copyright 2025 @Qreater
 Licensed under the Apache License, Version 2.0.
 See: http://www.apache.org/licenses/LICENSE-2.0
"""


from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from sqlalchemy.orm import Session

from dotenv import load_dotenv
from os import getenv

from core.model.user import User

from core.utils.database import save_and_refresh
from core.utils.errors import conflict_error, credential_error, not_found_error

load_dotenv()

SECRET_KEY = getenv("SECRET_KEY")
ALGORITHM = getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    """
    Get the hashed password.

    Args:
    password (str) : Plain password.

    Returns:
    str : Hashed password.
    """
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    """
    Verify the password with the hashed password.

    Args:
    plain_password (str) : Plain password.
    hashed_password (str) : Hashed password.

    Returns:
    bool : True if password matches, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict):
    """
    Create the access token.

    Args:
    data (dict) : Data to be encoded in the token.

    Returns:
    str : Encoded token.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str):
    """
    Decode the access token.

    Args:
    token (str) : Encoded token.

    Returns:
    dict : Decoded token.
    """

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.JWTError:
        return None


def check_user_exists(db: Session, email: str, username: str):
    """
    Check if user exists.

    Args:
    db (Session) : Database session.
    email (str) : Email address of user.
    username (str) : Username of user
    """

    user_email = db.query(User).filter(User.email == email).first()
    user_username = db.query(User).filter(User.username == username).first()
    if user_email is not None:
        raise conflict_error("User")
    if user_username is not None:
        raise conflict_error("Username")


def create_user(db: Session, email: str, password: str, username: str):
    """
    Create user.

    Args:
    db (Session) : Database session.
    email (str) : Email address of user.
    password (str) : Password of user.

    Returns:
    int : User id.
    """

    hashed_password = get_password_hash(password)

    user = User(email=email, password=hashed_password, username=username)
    save_and_refresh(db, user)

    return user.id


def verify_user(db: Session, username: str, password: str):
    """
    Verify the user.

    Args:
    db (Session) : Database session.
    email (str) : Email address of user.
    password (str) : Password of user.

    Returns:
    User : User object.
    """

    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise not_found_error("User")
    if not verify_password(password, user.password):
        raise credential_error("Password")
    return user
