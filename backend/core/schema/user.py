from pydantic import BaseModel, Field
from typing import Optional

class UserUpdate(BaseModel):
    description: Optional[str] = Field(example ="Welcome to my profile!", max_length=100)
    avatar_url: Optional[str] = Field(example ="https://example.com/avatar.png", max_length=100)

