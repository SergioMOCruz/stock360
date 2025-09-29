from fastapi import APIRouter, Depends, FastAPI, HTTPException
from starlette import status
from app.models import User, UserInToken
from app.routes.users.utils import get_current_user

router = APIRouter()

def get_app() -> FastAPI:
    from app.main import app
    return app

@router.get("/{user_id}", response_model=User)
async def get_user(
    user_id: str,
    app: FastAPI = Depends(get_app),
    current_user: UserInToken = Depends(get_current_user)
):
    if current_user.sub != user_id and current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only access your own user profile."
        )

    user = await app.mongodb["users"].find_one({"_id": user_id})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user["id"] = str(user["_id"])
    return User(**user)
