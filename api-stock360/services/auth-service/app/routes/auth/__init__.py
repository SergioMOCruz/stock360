from fastapi import APIRouter
from . import post, get, put, delete

router = APIRouter()
router.include_router(post.router, tags=["auth"])
