from fastapi import FastAPI

app = FastAPI(
    title="TallyTale",
    description="Polling through your next adventure.",
    version="0.1.0"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to TallyTale!"}


