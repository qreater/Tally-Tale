from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from core.utils.database import Base

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



