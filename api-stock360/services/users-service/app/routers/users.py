from fastapi import APIRouter, Depends, FastAPI
from ..models import User, UserCreate

router = APIRouter()

def get_app() -> FastAPI:
    from ..main import app
    return app

@router.post("/", response_model=User)
async def create_user(user: UserCreate, app: FastAPI = Depends(get_app)):
    result = await app.mongodb["users"].insert_one(user.dict())
    created_user = await app.mongodb["users"].find_one({"_id": result.inserted_id})
    created_user["id"] = str(created_user["_id"])
    return User(**created_user)

@router.get("/", response_model=list[User])
async def list_users(app: FastAPI = Depends(get_app)):
    users = []
    cursor = app.mongodb["users"].find({})
    async for user in cursor:
        user["id"] = str(user["_id"])
        users.append(User(**user))
    return users
