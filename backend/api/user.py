"""
 Copyright 2025 @Qreater
 Licensed under the Apache License, Version 2.0.
 See: http://www.apache.org/licenses/LICENSE-2.0
"""


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.utils.database import get_db
from core.utils.api.user import (
    get_user,
    update_user,
    delete_user,
    follow_user,
    unfollow_user,
    get_user_followers,
    get_user_following,
)

from core.utils.middlewares import authenticate_user

from core.schema.user import UserUpdate

router = APIRouter(tags=["me"], prefix="/me", dependencies=[Depends(authenticate_user)])


@router.get("/who/{username}")
async def get_user_details(username: str, db: Session = Depends(get_db)):
    """
    Get user details.

    Args:
    db (Session) : Database session.

    Returns:
    dict : A dictionary containing user details.
    """
    return get_user(db, username=username)


@router.put("/update")
async def update_user_description(
    request: UserUpdate,
    username: str = Depends(authenticate_user),
    db: Session = Depends(get_db),
):
    """
    Update user details.

    Args:
    request (UserUpdate) : User update details.
    db (Session) : Database session.

    Returns:
    dict : A dictionary containing user details.
    """
    return update_user(db, username=username, request=request)


@router.delete("/delete")
async def delete_user_account(
    username: str = Depends(authenticate_user), db: Session = Depends(get_db)
):
    """
    Delete user account.

    Args:
    token (str) : Access token.
    db (Session) : Database session.

    Returns:
    dict : A dictionary containing user details.
    """
    return delete_user(db, username=username)


@router.post("/follow/{username}")
async def follow_user_account(
    username: str,
    current_user: str = Depends(authenticate_user),
    db: Session = Depends(get_db),
):
    """
    Follow a user.

    Args:
    username (str) : The user's username.
    current_user (str) : The current user's username.
    db (Session) : Database session.

    Returns:
    dict : A dictionary containing user details.
    """
    return follow_user(db, username=current_user, following_username=username)


@router.post("/unfollow/{username}")
async def unfollow_user_account(
    username: str,
    current_user: str = Depends(authenticate_user),
    db: Session = Depends(get_db),
):
    """
    Unfollow a user.

    Args:
    username (str) : The user's username.
    current_user (str) : The current user's username.
    db (Session) : Database session.

    Returns:
    dict : A dictionary containing user details.
    """
    return unfollow_user(db, username=current_user, following_username=username)


@router.get("/followers")
def get_user_follower(
    username: str = Depends(authenticate_user),
    db: Session = Depends(get_db),
):
    """
    Get user followers.

    Args:
    username (str) : The user's username.
    db (Session) : Database session.

    Returns:
    dict : A dictionary containing user followers.
    """
    return get_user_followers(db, username=username)


@router.get("/following")
def get_usr_following(
    username: str = Depends(authenticate_user),
    db: Session = Depends(get_db),
):
    """
    Get user following.

    Args:
    username (str) : The user's username.
    db (Session) : Database session.

    Returns:
    dict : A dictionary containing user following.
    """
    return get_user_following(db, username=username)
