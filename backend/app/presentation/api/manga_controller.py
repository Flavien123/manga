from fastapi import APIRouter

router = APIRouter(prefix="/manga")

@router.get("/{id}")
async def get_manga_by_id():
    pass