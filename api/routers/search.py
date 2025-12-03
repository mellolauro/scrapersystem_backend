from fastapi import APIRouter, HTTPException
from typing import List

from api.models.search_request import SearchRequest
from api.models.job_result import SystemResult

from api.services.scraper_service import run_adherence_analysis 

router = APIRouter()

@router.post("/search", response_model=List[SystemResult])
def start_search(request: SearchRequest):
    """
    Recebe os critérios de busca e a matriz de aderência, 
    e inicia o processo de busca, scraping e pontuação.
    """
    try:
        results: List[SystemResult] = run_adherence_analysis(request)
        return results
    except Exception as e:
        print(f"Erro ao processar a busca: {e}")
        raise HTTPException(status_code=500, detail="Erro interno ao processar a busca.")

@router.get("/health")
def health_check():
    return {"status": "ok"}