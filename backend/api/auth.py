"""
 Copyright 2025 @Qreater
 Licensed under the Apache License, Version 2.0.
 See: http://www.apache.org/licenses/LICENSE-2.0
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from core.utils.api.auth import register, login
from core.utils.database import get_db

from core.schema.auth import RegisterRequest, LoginRequest


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/register")
def register_user(request: RegisterRequest, db: Session = Depends(get_db)):
    """
    Register a new user.

    Args:
    request (RegisterRequest) : User registration details.
    db (Session) : Database session.

    Returns:
    dict : A dictionary containing user details and an access token.
    """
    return register(db, request)


@router.post("/login")
def login_user(request: LoginRequest, db: Session = Depends(get_db)):
    """
    Login a user.

    Args:
    request (LoginRequest) : User login details.
    db (Session) : Database session.

    Returns:
    dict : A dictionary containing user details and an access token.
    """
    return login(db, request)
