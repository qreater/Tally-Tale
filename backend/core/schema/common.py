"""
 Copyright 2025 @Qreater
 Licensed under the Apache License, Version 2.0.
 See: http://www.apache.org/licenses/LICENSE-2.0
"""

from typing import Optional, Any, TypeVar, Generic
from pydantic import BaseModel, Field
from enum import Enum

T = TypeVar("T", bound=BaseModel)


class Status(str, Enum):
    """
    Enum class for status
    """

    success = "SUCCESS"
    error = "FAILURE"


class BaseResponse(BaseModel, Generic[T]):
    """
    Generic response class
    """

    status: Status = Field(Status.success, description="The status of the response.")
    message: Optional[str] = Field(None, description="The message for the response.")
    data: Optional[T] = Field(None, description="The data for the response.")
    errors: Optional[Any] = Field(None, description="The errors for the response.")
