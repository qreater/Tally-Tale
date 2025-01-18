"""
 Copyright 2025 @Qreater
 Licensed under the Apache License, Version 2.0.
 See: http://www.apache.org/licenses/LICENSE-2.0
"""


from fastapi import FastAPI
import os
from dotenv import load_dotenv

from core.utils.database import Base, engine

from api.auth import router as auth_router
from api.user import router as user_router

load_dotenv()

Base.metadata.create_all(bind=engine)

DATABASE_URI = os.getenv("DATABASE_URI")

app = FastAPI(
    title="TallyTale",
    description="Polling through your next adventure.",
    version="0.1.0",
)

app.include_router(auth_router)
app.include_router(user_router)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="FastAPI application",
        version="1.0.0",
        description="JWT Authentication and Authorization",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
    }
    openapi_schema["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema


@app.get("/")
def read_root():
    return {"message": "Welcome to TallyTale!"}
