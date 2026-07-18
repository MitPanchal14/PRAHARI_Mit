from fastapi import FastAPI

from app.api.incidents import router as incident_router

app = FastAPI(
    title="PRAHARI Backend",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to PRAHARI Backend"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


app.include_router(incident_router)