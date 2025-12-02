from fastapi import APIRouter, Depends
from api.models.search_request import SearchRequest
from api.core.worker_queue import task_queue
from api.services.scraper_service import run_scraper_job

router = APIRouter()

@router.post("/")
async def search_systems(search: SearchRequest):
    job_id = task_queue.enqueue(run_scraper_job, search.dict())
    return {"job_id": job_id}
