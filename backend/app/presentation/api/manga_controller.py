from fastapi import APIRouter

router = APIRouter(prefix="/manga")

@router.get("/{id}")
async def get_manga_by_id():
    pass

@router.get("/{id}/chapters")
async def get_manga_chapters_by_id():
    pass

@router.get("/{id}/chapters/{chapter_id}")
async def get_manga_chapter_by_id():
    pass

@router.get("/{id}/chapters/{chapter_id}/pages")
async def get_manga_chapter_pages_by_id():
    pass

@router.get("/{id}/chapters/{chapter_id}/pages/{page_id}")
async def get_manga_chapter_page_by_id():
    pass

