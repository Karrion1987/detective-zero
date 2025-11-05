
from fastapi import FastAPI
from .core.config import settings
from .core.db import init_db
from .routers import health as health_router
from .modules.cases.router import router as cases_router
from .modules.evidence.router import router as evidence_router
from .modules.ingest.router import router as ingest_router

app = FastAPI(title=settings.app_name)

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(health_router.router)
app.include_router(cases_router)
app.include_router(evidence_router)
app.include_router(ingest_router)

@app.get("/")
def root():
    return {"app": settings.app_name, "env": settings.env}
