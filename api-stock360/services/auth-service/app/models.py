from pydantic import BaseModel, EmailStr
from typing import Optional

class UserResponse(BaseModel):
    id: Optional[str]
    name: str
    email: EmailStr
    role: str

    class Config:
        validate_by_name = True
        json_encoders = {
        }

class UserInDB(UserResponse):
    password: str 

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"