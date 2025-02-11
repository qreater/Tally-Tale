"""
 Copyright 2025 @Qreater
 Licensed under the Apache License, Version 2.0.
 See: http://www.apache.org/licenses/LICENSE-2.0
"""

from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from datetime import datetime

from typing import Dict

from core.utils.exceptions.errors import not_found_error, conflict_error
from core.schema.story import StoryCreate, StoryUpdate
from core.model.story import Story


def create_story(db: Session, request: StoryCreate, username: str) -> dict:
    """
    Create a story.

    Args:
    db (Session) : Database session.
    request (StoryCreate) : Story creation details.

    Returns:
    dict : A dictionary containing story details.
    """
    story = Story(
        username=username,
        title=request.title,
        summary=request.summary,
        genre=request.genre,
        created_at=datetime.now(),
        updated_at=datetime.now(),
        tags=request.tags,
    )

    db.add(story)
    db.commit()

    return {
        "message": "Story created successfully",
        "details": {
            "id": story.id,
            "title": story.title,
            "username": story.username,
            "summary": story.summary,
            "genre": story.genre,
            "status": story.status,
            "created_at": story.created_at,
            "updated_at": story.updated_at,
            "tags": story.tags,
        },
    }


def get_story(db: Session, story_id: str) -> dict:
    """
    Get a story by id.

    Args:
    db (Session) : Database session.
    story_id (int) : Story id.

    Returns:
    dict : A dictionary containing story details.
    """
    story = db.query(Story).filter(Story.id == story_id).first()

    if not story:
        raise not_found_error("Story")

    return {
        "title": story.title,
        "summary": story.summary,
        "genre": story.genre,
        "status": story.status,
        "created_at": story.created_at,
        "updated_at": story.updated_at,
        "tags": story.tags,
    }


def update_story(db: Session, story_id: str, request: StoryUpdate) -> dict:
    """
    Update a story.

    Args:
    db (Session) : Database session.
    story_id (str) : Story id.
    title (str) : New title.
    """
    story = db.query(Story).filter(Story.id == story_id).first()

    if not story:
        raise not_found_error("Story")

    update_data = request.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(story, key, value)
    story.updated_at = datetime.utcnow()

    db.commit()
    db.refresh(story)

    return {
        "message": "Story updated successfully",
        "details": {
            "id": story.id,
            "title": story.title,
            "summary": story.summary,
            "genre": story.genre,
            "status": story.status,
            "created_at": story.created_at,
            "updated_at": story.updated_at,
            "tags": story.tags,
        },
    }


def delete_story(db: Session, story_id: str):
    """
    Delete a story.

    Args:
    db (Session) : Database session.
    story_id (int) : Story id.
    """
    story = db.query(Story).filter(Story.id == story_id).first()

    if not story:
        raise not_found_error("Story")

    db.delete(story)
    db.commit()

    return {
        "message": "Story deleted successfully",
    }


def get_all_stories(
    db: Session,
    skip: int = 0,
    limit: int = 10,
    username: str = None,
    tag: str = None,
    genre: str = None,
    chapter_no: int = 0,
) -> list:
    """
    Get all stories.

    Args:
    db (Session) : Database session.
    skip (int) : Number of stories to skip.
    limit (int) : Number of stories to return.
    username (str) : Story author's username.
    tag (str) : Story tag.
    genre (str) : Story genre.
    chapter_no (int) : Story chapter number.

    Returns:
    list : A list of dictionaries containing story details.
    """
    base_query = db.query(Story)

    filters = []

    if username:
        filters.append(Story.username.ilike(f"%{username}%"))

    if tag:
        filters.append(Story.tags.any(tag))

    if genre:
        filters.append(Story.genre.any(genre))

    if chapter_no > 0:
        filters.append(Story.chapter_no >= chapter_no)

    if filters:
        base_query = base_query.filter(and_(*filters))

    stories = (
        base_query.order_by(Story.created_at.desc()).offset(skip).limit(limit).all()
    )

    return {
        "message": "Stories retrieved successfully",
        "details": [
            {
                "id": story.id,
                "title": story.title,
                "summary": story.summary,
                "genre": story.genre,
                "status": story.status,
                "created_at": story.created_at,
                "updated_at": story.updated_at,
                "tags": story.tags,
            }
            for story in stories
        ],
    }
