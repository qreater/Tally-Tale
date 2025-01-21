"""
 Copyright 2025 @Qreater
 Licensed under the Apache License, Version 2.0.
 See: http://www.apache.org/licenses/LICENSE-2.0
"""


from fastapi import FastAPI
import logging
import logging.config

from core.utils.database import Base, engine

from core.utils.exceptions.errors import APIError
from core.utils.exceptions.logger import get_log_config
from core.utils.exceptions.handler import ErrorHandlingMiddleware, api_error_handler


from api.auth import router as auth_router
from api.user import router as user_router


Base.metadata.create_all(bind=engine)

logging.config.dictConfig(get_log_config())

app = FastAPI(
    title="TallyTale",
    description="Polling through your next adventure.",
    version="0.1.0",
)

app.add_exception_handler(APIError, api_error_handler)
app.add_middleware(ErrorHandlingMiddleware)


app.include_router(auth_router)
app.include_router(user_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to TallyTale!"}
