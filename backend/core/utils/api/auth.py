from core.schema.auth import RegisterRequest, LoginRequest
from sqlalchemy.orm import Session

from core.utils.auth import (
    create_access_token, 
    check_user_exists, 
    create_user, 
    verify_password, 
    get_password_hash,
    verify_user,
)

def register(db: Session, request: RegisterRequest) -> dict:
    """
    Register a new user.

    Args:
    db (Session) : Database session.
    request (RegisterRequest) : User registration details.

    Returns:
    dict : A dictionary containing user details and an access token.
    """
    check_user_exists(db, request.email, request.username)

    user = create_user(db, request.email, request.password, request.username)
    data = {
        "username": request.username,
    }
    access_token = create_access_token(data)

    return {
        "message": "User created successfully",
        "access_token": access_token,
        "details": {
            "email": request.email,
            "username": request.username,
        },
    }

def login(db: Session, request: LoginRequest) -> dict:
    """
    Login a user.

    Args:
    db (Session) : Database session.
    request (LoginRequest) : User login details.

    Returns:
    dict : A dictionary containing user details and an access token.
    """
    user = verify_user(db, request.username, request.password)
    data = {
        "username": user.username,
    }
    access_token = create_access_token(data)

    return {
        "message": "Login successful",
        "access_token": access_token,
        "details": {
            "email": user.email,
            "username": user.username,
        },
    }
 