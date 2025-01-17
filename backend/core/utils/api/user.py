from sqlalchemy.orm import Session

from core.utils.errors import not_found_error
from core.schema.user import UserUpdate
from core.model.user import User


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