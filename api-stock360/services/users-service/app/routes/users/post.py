from app.models import User, UserCreate
from fastapi import APIRouter, Depends, FastAPI, HTTPException

router = APIRouter()


def get_app() -> FastAPI:
    from app.main import app

    return app


@router.post("/", response_model=User, include_in_schema=False)
async def create_user(user: UserCreate, app: FastAPI = Depends(get_app)):
    new_user_data = user.dict()
    new_user_data["_id"] = new_user_data.pop("id", None)
    if new_user_data["_id"] is None:
        raise HTTPException(status_code=400, detail="User ID must be provided.")
    await app.mongodb["users"].insert_one(new_user_data)

    created_user = await app.mongodb["users"].find_one({"_id": new_user_data["_id"]})
    created_user["id"] = str(created_user["_id"])
    return User(**created_user)
