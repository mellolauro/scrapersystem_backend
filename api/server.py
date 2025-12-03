# server.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers import search

app = FastAPI()

# Permitir o Next.js acessar o FastAPI
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(search.router)
