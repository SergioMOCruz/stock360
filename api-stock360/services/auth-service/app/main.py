from fastapi import FastAPI
from .database import init_db, close_db
from .routes.auth import router as auth_router

app = FastAPI(title="Auth Service")

@app.on_event("startup")
async def startup_event():
    init_db(app)

@app.on_event("shutdown")
async def shutdown_event():
    close_db(app)

@app.get("/")
def health():
    return {"status": "ok", "service": "auth"}

app.include_router(auth_router, prefix="/auth")
