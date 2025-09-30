from fastapi import APIRouter
from . import post, get

router = APIRouter()
router.include_router(post.router, tags=["users"])
router.include_router(get.router, tags=["users"])

## router.include_router(put.router, tags=["users"])
## router.include_router(delete.router, tags=["users"])
