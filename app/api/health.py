from fastapi import APIRouter
from sqlalchemy import text

from app.db.session import engine


router = APIRouter()


@router.get("/database")
def database_health():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "database": "postgresql",
            "status": "connected",
        }

    except Exception as exc:
        return {
            "database": "postgresql",
            "status": "error",
            "detail": str(exc),
        }