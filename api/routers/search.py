# routers/search.py
from fastapi import APIRouter

router = APIRouter()

@router.post("/search")
async def search(query: dict):
    # seu scraping aqui
    return {"results": [{"title": "teste", "url": "https://exemplo.com", "rank": 1}]}
