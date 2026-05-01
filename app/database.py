import os
from functools import lru_cache

from motor.motor_asyncio import AsyncIOMotorClient

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
DATABASE_NAME = "merge_practice_branch_12"
USERS_COLLECTION = "users_branch_12"
CONNECTION_LABEL = "conflict-12-connection"


@lru_cache
def get_client() -> AsyncIOMotorClient:
    return AsyncIOMotorClient(MONGODB_URI, appname=CONNECTION_LABEL)


def get_database():
    return get_client()[DATABASE_NAME]


def get_users_collection():
    return get_database()[USERS_COLLECTION]
