from fastapi import FastAPI, HTTPException

from app.database import get_users_collection
from app.models import UserCreate, UserOut

app = FastAPI(
    title="FastAPI Mongo Practice API",
    version="0.1.0",
    description="Main branch API used as the starting point for merge conflict practice.",
)

API_PREFIX = "/api/v1"
DEFAULT_ROLE = "reader"
WELCOME_MESSAGE = "Hello from the main branch FastAPI service."


@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "main", "database": "merge_practice"}


@app.post(f"{API_PREFIX}/users", response_model=UserOut)
async def create_user(payload: UserCreate):
    users = get_users_collection()
    existing = await users.find_one({"email": payload.email})
    if existing:
        raise HTTPException(status_code=409, detail="User already exists")

    document = payload.model_dump()
    document["role"] = DEFAULT_ROLE
    document["welcome_message"] = WELCOME_MESSAGE
    result = await users.insert_one(document)
    document["id"] = str(result.inserted_id)
    return UserOut(**document)
