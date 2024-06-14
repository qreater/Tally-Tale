from fastapi import FastAPI
import os
from pymongo import MongoClient
from dotenv import load_dotenv
app = FastAPI(
    title="TallyTale",
    description="Polling through your next adventure.",
    version="0.1.0"
)

load_dotenv()
MONGO_URL = os.getenv('MONGO_URI')

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(MONGO_URL, uuidRepresentation="standard")
    database = app.mongodb_client["TallyTales"]
    app.tales_collection = database.get_collection("TallyTale")
    server_info = app.mongodb_client.server_info()
    print(f"Connected to MongoDB server {server_info['version']}")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to TallyTale!"}

