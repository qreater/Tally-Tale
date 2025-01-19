"""
 Copyright 2025 @Qreater
 Licensed under the Apache License, Version 2.0.
 See: http://www.apache.org/licenses/LICENSE-2.0
"""


from fastapi import Request, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from core.model.user import User

from core.utils.auth import decode_access_token
from core.utils.errors import unauthorized_error, credential_error
from core.utils.database import get_db


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def authenticate_user(
    request: Request, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    """
    Authenticate the user.

    Args:
    request (Request) : Request object.
    token (str) : Access token.
    db (Session) : Database session.
    """
    if not token:
        raise unauthorized_error()
    token_data = decode_access_token(token)

    user = db.query(User).filter(User.username == token_data["username"]).first()
    if not user:
        raise credential_error()

    return user.username
