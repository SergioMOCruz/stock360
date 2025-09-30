from fastapi import APIRouter, Depends, HTTPException, FastAPI
from ..models import LoginRequest, TokenResponse, UserCreate, UserInDB
from ..security import create_access_token, hash_password, verify_password 
from bson import ObjectId
import httpx

router = APIRouter()

def get_app() -> FastAPI:
    from ..main import app
    return app

@router.post("/register", response_model=UserInDB)
async def register(user: UserCreate, app: FastAPI = Depends(get_app)):
    existing = await app.mongodb["users"].find_one({"email": user.email})
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = user.dict()
    new_user["password"] = hash_password(new_user["password"])
    new_user["role"] = "user"

    new_user["_id"] = new_user.pop("id", str(ObjectId()))

    result = await app.mongodb["users"].insert_one(new_user)

    if result.inserted_id:
        created = await app.mongodb["users"].find_one({"_id": new_user["_id"]})

        if created:
            created["id"] = str(created["_id"])

            async with httpx.AsyncClient() as client:
                await client.post(
                    "http://users-service:8000/users/",
                    json={"id": created["id"], "name": user.name, "email": user.email, "role": "user"}
                )

            return UserInDB(**created)
        else:
            raise Exception("User inserted but failed to retrieve immediately after.")
    else:
        raise Exception("Failed to insert user into the database.")


@router.post("/login", response_model=TokenResponse)
async def login(request: LoginRequest, app: FastAPI = Depends(get_app)):
    user = await app.mongodb["users"].find_one({"email": request.email})
    
    if not user or not verify_password(request.password, user["password"]): 
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": str(user["_id"]), "role": user.get("role", "user")})
    return TokenResponse(access_token=token)