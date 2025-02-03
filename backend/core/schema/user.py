"""
 Copyright 2025 @Qreater
 Licensed under the Apache License, Version 2.0.
 See: http://www.apache.org/licenses/LICENSE-2.0
"""


from pydantic import BaseModel, Field
from typing import Optional


class UserUpdate(BaseModel):
    """
    Schema for updating user profile

    Attributes:
    -----------
    username: str
        The username of the user
    description: str
        The description of the user
    avatar_url: str
        The URL of the user's avatar

    """

    description: Optional[str] = Field(example="Welcome to my profile!", max_length=100)
    avatar_url: Optional[str] = Field(
        example="https://example.com/avatar.png", max_length=100
    )
