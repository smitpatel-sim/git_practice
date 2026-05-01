from fastapi import FastAPI, HTTPException

from app.database import get_users_collection
from app.models import UserCreate, UserOut

app = FastAPI(
    title="FastAPI Mongo Branch 05 API",
    version="0.5.0",
    description="Conflict branch 05 changes API metadata, defaults, and response behavior.",
)

API_PREFIX = "/api/branch-05"
DEFAULT_ROLE = "admin"
WELCOME_MESSAGE = "Hello from conflict branch 05; resolve this with care."


@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "conflict-05", "database": "merge_practice_branch_05"}


@app.post(f"{API_PREFIX}/users", response_model=UserOut)
async def create_user(payload: UserCreate):
    users = get_users_collection()
    existing = await users.find_one({"email": payload.email})
    if existing:
        raise HTTPException(status_code=409, detail="User already exists on conflict-05")

    document = payload.model_dump()
    document["role"] = DEFAULT_ROLE
    document["welcome_message"] = WELCOME_MESSAGE
    result = await users.insert_one(document)
    document["id"] = str(result.inserted_id)
    return UserOut(**document)
