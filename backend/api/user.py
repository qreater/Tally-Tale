from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.utils.database import get_db
from core.utils.api.user import get_user, update_user, delete_user

from core.utils.middlewares import authenticate_user

from core.schema.user import UserUpdate

router = APIRouter(
    tags=["me"],
    prefix="/me",
    dependencies=[Depends(authenticate_user)]
)

@router.get("/{username}")
async def get_user_details(
    username: str,
    db: Session = Depends(get_db)
  ):
    """
    Get user details.
    
    Args:
    db (Session) : Database session.
    
    Returns:
    dict : A dictionary containing user details.
    """
    return get_user(db, username= username)

@router.put("/update")
async def update_user_description(
    request: UserUpdate,
    username: str = Depends(authenticate_user), 
    db: Session = Depends(get_db)
    ):
    """
    Update user details.
    
    Args:
    request (UserUpdate) : User update details.
    db (Session) : Database session.
    
    Returns:
    dict : A dictionary containing user details.
    """
    return update_user(db, username= username, request=request)


@router.delete("/delete")
async def delete_user_account(
    username: str = Depends(authenticate_user),
    db: Session = Depends(get_db)
    ):
    """
    Delete user account.
    
    Args:
    token (str) : Access token.
    db (Session) : Database session.
    
    Returns:
    dict : A dictionary containing user details.
    """
    return delete_user(db, username= username)    