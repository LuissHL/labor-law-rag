from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()


@router.get("/health", status_code=200)
def health_check() -> dict[str, str]:
    """
    Endpoint para verificação da saúde da API.
    Returns:
        dict[str, str]: Um dicionário contendo o status da API, o nome do projeto e o ambiente.
    """
    return {
        "status": "healthy",
        "project_name": settings.PROJECT_NAME,
        "environment": settings.ENVIRONMENT,
    }