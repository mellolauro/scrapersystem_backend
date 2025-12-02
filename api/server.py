from fastapi import FastAPI
from api.routers import health, search

app = FastAPI(title="Scraper API", version="1.0.0")

# Registrar rotas
app.include_router(health.router, prefix="/health", tags=["Health"])
app.include_router(search.router, prefix="/search", tags=["Search"])

@app.get("/")
def root():
    return {"message": "API online"}
