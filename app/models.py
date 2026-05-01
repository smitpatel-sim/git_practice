from pydantic import BaseModel, EmailStr, Field

USERNAME_MIN_LENGTH = 4
USERNAME_MAX_LENGTH = 30
DEFAULT_PLAN = "growth"
PROFILE_SOURCE = "conflict-06"


class UserCreate(BaseModel):
    username: str = Field(min_length=USERNAME_MIN_LENGTH, max_length=USERNAME_MAX_LENGTH)
    email: EmailStr
    display_name: str = Field(min_length=1, max_length=66)
    plan: str = DEFAULT_PLAN


class UserOut(UserCreate):
    id: str
    role: str
    welcome_message: str
    source: str = PROFILE_SOURCE
