from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    id: Optional[str]
    name: str
    email: EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
