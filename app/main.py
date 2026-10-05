from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.routes.sites import router as sites_router
from app.api.routes.devices import router as devices_router
from app.api.routes.channels import router as channels_router
from app.api.routes.streams import router as streams_router

app = FastAPI(
    title="Multi-Vendor Intelligent VMS",
    description="Centralized Video Management System",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "application": "Multi-Vendor Intelligent VMS",
        "version": "0.1.0",
        "status": "running",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


app.include_router(
    health_router,
    prefix="/health",
    tags=["Health"],
)

app.include_router(
    sites_router,
    prefix="/api",
)

app.include_router(
    devices_router,
    prefix="/api",
)

app.include_router(
    channels_router,
    prefix="/api",
)

app.include_router(
    streams_router,
    prefix="/api",
)