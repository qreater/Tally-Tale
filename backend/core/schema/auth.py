from pydantic import BaseModel

class RegisterRequest(BaseModel):
    """
    Schema for user authentication details
    
    Attributes:
    -----------
    username: str
        The user's username
    password: str
        The user's password
    email: str
        The user's email
    description: str
        The user's description
    avatar_url: str
        The user's avatar URL    
    """
    username: str
    password: str
    email: str


class LoginRequest(BaseModel):
    """
    Schema for user login details
    
    Attributes:
    -----------
    username: str
        The user's username
    password: str
        The user's password
    """
    username: str
    password: str
