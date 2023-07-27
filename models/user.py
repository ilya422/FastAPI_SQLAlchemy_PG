from typing import Optional

from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: Optional[str]
    city_id: int


class User(UserCreate):
    id: int

