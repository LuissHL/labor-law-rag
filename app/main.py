from fastapi import FastAPI
from app.api.routes import health
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Registra os roteadores da API
app.include_router(health.router, tags=["Health"])


@app.get("/")
def root() -> dict[str, str]:
    return {"message": f"Bem-vindo à API do {settings.PROJECT_NAME}"}