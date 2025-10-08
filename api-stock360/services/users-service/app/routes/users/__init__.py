from fastapi import APIRouter

from . import get, post

router = APIRouter()
router.include_router(post.router, tags=["users"])
router.include_router(get.router, tags=["users"])
