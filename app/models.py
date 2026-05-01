from pydantic import BaseModel, EmailStr, Field

USERNAME_MIN_LENGTH = 3
USERNAME_MAX_LENGTH = 29
DEFAULT_PLAN = "starter"
PROFILE_SOURCE = "conflict-05"


class UserCreate(BaseModel):
    username: str = Field(min_length=USERNAME_MIN_LENGTH, max_length=USERNAME_MAX_LENGTH)
    email: EmailStr
    display_name: str = Field(min_length=1, max_length=65)
    plan: str = DEFAULT_PLAN


class UserOut(UserCreate):
    id: str
    role: str
    welcome_message: str
    source: str = PROFILE_SOURCE
