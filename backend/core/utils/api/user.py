"""
 Copyright 2025 @Qreater
 Licensed under the Apache License, Version 2.0.
 See: http://www.apache.org/licenses/LICENSE-2.0
"""


from sqlalchemy.orm import Session

from core.utils.exceptions.errors import not_found_error, conflict_error
from core.schema.user import UserUpdate
from core.model.user import User, followers_association


def get_user(db: Session, username: str) -> dict:
    """
    Get a user.

    Args:
    db (Session) : Database session.
    username (str) : The user's username.

    Returns:
    dict : A dictionary containing user details.
    """
    user = db.query(User).filter(User.username == username).first()

    if not user:
        not_found_error("User")

    return {
        "message": "User retrieved successfully",
        "details": {
            "username": user.username,
            "email": user.email,
            "description": user.description,
            "avatar_url": user.avatar_url,
        },
    }


def update_user(db: Session, username: str, request: UserUpdate) -> dict:
    """
    Update a user.

    Args:
    db (Session) : Database session.
    username (str) : The user's username.
    request (UpdateUserRequest) : User update details.

    Returns:
    dict : A dictionary containing user details.
    """
    user = db.query(User).filter(User.username == username).first()

    if not user:
        not_found_error("User")

    user.description = request.description
    user.avatar_url = request.avatar_url

    db.commit()

    return {
        "message": "User updated successfully",
        "details": {
            "username": user.username,
            "email": user.email,
            "description": user.description,
            "avatar_url": user.avatar_url,
        },
    }


def delete_user(db: Session, username: str) -> dict:
    """
    Delete a user.

    Args:
    db (Session) : Database session.
    username (str) : The user's username.

    Returns:
    dict : A dictionary containing a success message.
    """
    user = db.query(User).filter(User.username == username).first()

    if not user:
        not_found_error("User")

    db.delete(user)
    db.commit()

    return {
        "message": "User deleted successfully",
    }


def follow_user(db: Session, username: str, following_username: str) -> dict:
    """
    Follow a user.

    Args:
    db (Session) : Database session.
    username (str) : The user's username.
    following_username (str) : The username of the user to follow.

    Returns:
    dict : A dictionary containing a success message.
    """

    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise not_found_error("User")
    following_user = db.query(User).filter(User.username == following_username).first()
    if not following_user:
        raise not_found_error("User to follow")

    is_following = (
        db.query(followers_association)
        .filter(
            followers_association.c.follower_id == user.id,
            followers_association.c.following_id == following_user.id,
        )
        .first()
    )

    if is_following is None:
        raise conflict_error("The following")

    new_follow = followers_association.insert().values(
        follower_id=user.id, following_id=following_user.id
    )
    db.execute(new_follow)

    user.following_count += 1
    following_user.followers_count += 1

    db.commit()

    return {
        "message": "User followed successfully",
    }


def unfollow_user(db: Session, username: str, following_username: str) -> dict:
    """
    Unfollow a user.

    Args:
    db (Session) : Database session.
    username (str) : The user's username.
    following_username (str) : The username of the user to unfollow.

    Returns:
    dict : A dictionary containing a success message.
    """
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise not_found_error("User")
    following_user = db.query(User).filter(User.username == following_username).first()
    if not following_user:
        raise not_found_error("User to unfollow")

    is_following = (
        db.query(followers_association)
        .filter(
            followers_association.c.follower_id == user.id,
            followers_association.c.following_id == following_user.id,
        )
        .first()
    )

    if is_following is None:
        raise conflict_error("No following")

    db.execute(
        followers_association.delete().where(
            followers_association.c.follower_id == user.id,
            followers_association.c.following_id == following_user.id,
        )
    )

    user.following_count -= 1
    following_user.followers_count -= 1

    db.commit()

    return {
        "message": "User unfollowed successfully",
    }


def get_user_followers(db: Session, username: str) -> dict:
    """
    Get a user's followers.

    Args:
    db (Session) : Database session.
    username (str) : The user's username.

    Returns:
    dict : A dictionary containing user details.
    """
    user = db.query(User).filter(User.username == username).first()

    if not user:
        not_found_error("User")

    followers_data = [
        {
            "username": follower.username,
            "description": follower.description,
        }
        for follower in user.followers
    ]

    return {
        "message": "User followers retrieved successfully",
        "details": {
            "followers": {
                "count": user.followers_count,
                "details": followers_data,
            }
        },
    }


def get_user_following(db: Session, username: str) -> dict:
    """
    Get a user's following.

    Args:
    db (Session) : Database session.
    username (str) : The user's username.

    Returns:
    dict : A dictionary containing user details.
    """
    user = db.query(User).filter(User.username == username).first()

    if not user:
        not_found_error("User")

    return {
        "message": "User following retrieved successfully",
        "details": {
            "following": {
                "count": user.following_count,
                "details": [
                    {
                        "username": following.username,
                        "description": following.description,
                    }
                    for following in user.following
                ],
            },
        },
    }
