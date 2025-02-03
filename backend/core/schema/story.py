"""
 Copyright 2025 @Qreater
 Licensed under the Apache License, Version 2.0.
 See: http://www.apache.org/licenses/LICENSE-2.0
"""

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class StoryCreate(BaseModel):
    """
    Schema for creating a new story

    Attributes:
    -----------
    title: str
        The title of the story
    summary: str
        The summary of the story
    genre: list
        The genre of the story
    tags: list
        The tags of the story

    """

    title: str = Field(..., max_length=100)
    summary: str = Field(..., max_length=500)
    genre: list = Field()
    tags: list = Field()


class StoryUpdate(BaseModel):
    """
    Schema for updating a story

    Attributes:
    -----------
    title: str
        The title of the story
    summary: str
        The summary of the story
    genre: list
        The genre of the story
    tags: list
        The tags of the story

    """

    title: Optional[str] = Field(None, max_length=255)
    summary: Optional[str] = Field(None, max_length=500)
    genre: Optional[List[str]] = []
    status: Optional[str] = Field(None, max_length=50)
    tags: Optional[List[str]] = []

    class Config:
        orm_mode = True


class StoryRead(BaseModel):
    """
    Schema for reading a story

    Attributes:
    -----------
    id: int
        The id of the story
    title: str
        The title of the story
    user_id: int
        The id of the user who created the story
    summary: str
        The summary of the story
    genre: list
        The genre of the story
    created_at: datetime
        The date and time the story was created
    updated_at: datetime
        The date and time the story was last updated
    tags: list
        The tags of the story
    status: str
        The status of the story

    """

    title: str = Field(..., max_length=100)
    user_id: int = Field(..., example=1)
    summary: str = Field(..., max_length=500)
    genre: list = Field()
    created_at: datetime = Field(..., example=datetime.now())
    updated_at: datetime = Field(..., example=datetime.now())
    tags: list = Field()
    status: str = Field(..., example="draft")
