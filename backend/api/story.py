"""
 Copyright 2025 @Qreater
 Licensed under the Apache License, Version 2.0.
 See: http://www.apache.org/licenses/LICENSE-2.0
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.utils.database import get_db
from core.utils.api.story import (
    get_story,
    create_story,
    update_story,
    delete_story,
    get_all_stories,
)

from core.utils.middlewares import authenticate_user

from core.schema.story import StoryCreate, StoryUpdate

router = APIRouter(
    tags=["story"], prefix="/story", dependencies=[Depends(authenticate_user)]
)


@router.post("/create")
async def create_new_story(
    request: StoryCreate,
    username: str = Depends(authenticate_user),
    db: Session = Depends(get_db),
):
    """
    Create a new story.

    Args:
    request (StoryCreate) : Story creation details.
    db (Session) : Database session.

    Returns:
    dict : A dictionary containing story details.
    """
    return create_story(db, request, username)


@router.get("/get/{story_id}")
async def get_story_details(story_id: str, db: Session = Depends(get_db)):
    """
    Get story details.

    Args:
    story_id (str) : Story id.
    db (Session) : Database session.

    Returns:
    dict : A dictionary containing story details.
    """
    return get_story(db, story_id)


@router.put("/update/{story_id}")
def update_stories(story_id: str, request: StoryUpdate, db: Session = Depends(get_db)):
    """
    Update story.

    Args:
    story_id (str) : Story id.
    request (StoryUpdate) : Story update details.
    db (Session) : Database session.

    Returns:
    dict : A dictionary containing story details.
    """
    return update_story(db, story_id, request)


@router.delete("/delete/{story_id}")
async def delete_story_account(story_id: str, db: Session = Depends(get_db)):
    """
    Delete story.

    Args:
    story_id (str) : Story id.
    db (Session) : Database session.

    Returns:
    dict : A dictionary containing story details.
    """
    return delete_story(db, story_id)


@router.get("/all")
async def get_all_story(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 10,
    username: str = None,
    tag: str = None,
    genre: str = None,
    chapter_no: int = 0,
):
    """
    Get all stories.

    Args:
    db (Session) : Database session.

    Returns:
    dict : A dictionary containing all stories.
    """
    return get_all_stories(
        db,
        skip=skip,
        limit=limit,
        username=username,
        tag=tag,
        genre=genre,
        chapter_no=chapter_no,
    )
