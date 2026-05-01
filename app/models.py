from pydantic import BaseModel, EmailStr, Field

USERNAME_MIN_LENGTH = 5
USERNAME_MAX_LENGTH = 31
DEFAULT_PLAN = "pro"
PROFILE_SOURCE = "conflict-07"


class UserCreate(BaseModel):
    username: str = Field(min_length=USERNAME_MIN_LENGTH, max_length=USERNAME_MAX_LENGTH)
    email: EmailStr
    display_name: str = Field(min_length=1, max_length=67)
    plan: str = DEFAULT_PLAN


class UserOut(UserCreate):
    id: str
    role: str
    welcome_message: str
    source: str = PROFILE_SOURCE
