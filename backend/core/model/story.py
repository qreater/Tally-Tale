"""
 Copyright 2025 @Qreater
 Licensed under the Apache License, Version 2.0.
 See: http://www.apache.org/licenses/LICENSE-2.0
"""

from sqlalchemy import Table, Column, ForeignKey, Integer, String, Index, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy.orm import relationship
from uuid import uuid4

from typing import List

from core.utils.database import Base


class Story(Base):
    """
    Story model

    Attributes:
    -----------
    id: int
        The story's unique identifier
    title: str
        The story's title
    summary: str
        The story's summary
    user_id: int
        The story's author's unique identifier
    genre: list
        The story's genre
    created_at: datetime
        The story's creation date
    updated_at: datetime
        The story's last update date
    tags: list
        The story's tags
    status: str
        The story's status
    chapter_no: int
        The story's chapter number

    """

    __tablename__ = "story"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, index=True)
    title = Column(String, index=True)
    summary = Column(Text)
    username = Column(String, ForeignKey("user.username"), index=True)
    genre = Column(ARRAY(String(50)), index=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    tags = Column(ARRAY(String(50)), index=True)
    status = Column(String, index=True, default="Ongoing")
    chapter_no = Column(Integer, index=True, default=0)
