"""
 Copyright 2025 @Qreater
 Licensed under the Apache License, Version 2.0.
 See: http://www.apache.org/licenses/LICENSE-2.0
"""


from sqlalchemy import Table, Column, ForeignKey, Integer, String, Index
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from uuid import uuid4

from core.utils.database import Base

followers_association = Table(
    "followers_association",
    Base.metadata,
    Column("follower_id", UUID(as_uuid=True), ForeignKey("user.id")),
    Column("following_id", UUID(as_uuid=True), ForeignKey("user.id")),
    Index("ix_follower_id", "follower_id"),
    Index("ix_following_id", "following_id"),
)


class User(Base):
    """
    User model

    Attributes:
    -----------
    id: UUID
        The user's unique identifier
    username: str
        The user's username
    email: str
        The user's email
    password: str
        The user's password
    description: str
        The user's description
    avatar_url: str
        The user's avatar URL
    """

    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    description = Column(String, default=f"Hi, I'm {username}!")
    avatar_url = Column(String, default="./doc-assets/image.png")

    followers_count = Column(Integer, default=0)
    following_count = Column(Integer, default=0)

    followers = relationship(
        "User",
        secondary=followers_association,
        primaryjoin=id == followers_association.c.following_id,
        secondaryjoin=id == followers_association.c.follower_id,
        backref="following",
    )
