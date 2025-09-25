from fastapi import FastAPI
from .database import init_db, close_db
from .routers import users
from .models import User, UserCreate

app = FastAPI(title="Users Service")

@app.on_event("startup")
async def startup_event():
    init_db(app)

@app.on_event("shutdown")
async def shutdown_event():
    close_db(app)

@app.get("/")
def health():
    return {"status": "ok", "service": "users"}

# Include router
app.include_router(users.router, prefix="/users", tags=["users"])
