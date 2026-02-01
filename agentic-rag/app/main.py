from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Agentic RAG API")

app.include_router(router)
