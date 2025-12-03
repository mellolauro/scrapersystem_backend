from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers import search, health

app = FastAPI()

# Defina as origens permitidas
origins = [
    "http://localhost",  # Permite requisições diretas ao Caddy (porta 80)
    "http://localhost:3000",  # Permite requisições do frontend Next.js
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Permite OPTIONS, GET, POST, etc.
    allow_headers=["*"],
)

app.include_router(search.router, tags=["Search"], prefix="/api/v1")
app.include_router(health.router, tags=["Health"])