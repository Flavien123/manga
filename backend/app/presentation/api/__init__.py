from fastapi import APIRouter

from .manga_controller import router as manga_router

router = APIRouter(prefix="/api")

router.include_router(router=manga_router)