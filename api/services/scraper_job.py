# api/services/scraper_job.py

from api.services.scraper_service import search_softwares
from api.services.score_service import calculate_score
from api.core.worker_queue import redis_conn
import json
import uuid

def run_scraper_job(payload: dict):
    """
    Job principal processado pelo worker.
    Ele recebe o título e a matriz de aderência e retorna
    uma lista dos melhores softwares encontrados + score.
    """

    job_id = payload.get("job_id", str(uuid.uuid4()))
    title = payload["title"]
    requirements = payload["requirements"]

    # 1. Buscar softwares
    softwares = search_softwares(title)

    # 2. Calcular score para cada software
    results = []

    for s in softwares:
        score_data = calculate_score(s["description"], requirements)

        results.append({
            "software": s["name"],
            "empresa": s.get("company", "Desconhecido"),
            "url": s.get("url"),
            "score": score_data["score"],
            "matched": score_data["matched"],
            "unmatched": score_data["unmatched"],
        })

    # 3. Ordenar ranking
    results.sort(key=lambda x: x["score"], reverse=True)

    # 4. Salvar resultado no Redis
    redis_conn.set(f"result:{job_id}", json.dumps(results))

    return {"job_id": job_id}
