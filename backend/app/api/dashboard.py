from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.dashboard_service import DashboardService

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/stats")
def dashboard_stats(db: Session = Depends(get_db)):
    return DashboardService.stats(db)


@router.get("/recent-incidents")
def recent_incidents(db: Session = Depends(get_db)):
    return DashboardService.recent(db)


@router.get("/high-risk")
def high_risk(db: Session = Depends(get_db)):
    return DashboardService.high_risk(db)


@router.get("/open")
def open_cases(db: Session = Depends(get_db)):
    return DashboardService.open_cases(db)


@router.get("/analytics")
def analytics(db: Session = Depends(get_db)):
    return DashboardService.analytics(db)