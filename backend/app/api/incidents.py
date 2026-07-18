from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.incident import IncidentCreate, IncidentUpdate, IncidentResponse
from app.services.incident_service import IncidentService

router = APIRouter(prefix="/api", tags=["Incidents"])


@router.post("/incidents", response_model=IncidentResponse)
def create_incident(
    data: IncidentCreate,
    db: Session = Depends(get_db)
):
    return IncidentService.create_incident(db, data)


@router.get("/incidents", response_model=list[IncidentResponse])
def get_incidents(
    db: Session = Depends(get_db)
):
    return IncidentService.get_incidents(db)


@router.get("/incidents/{incident_id}", response_model=IncidentResponse)
def get_incident(
    incident_id: str,
    db: Session = Depends(get_db)
):

    incident = IncidentService.get_incident(db, incident_id)

    if not incident:
        raise HTTPException(
            status_code=404,
            detail="Incident not found"
        )

    return incident


@router.delete("/incidents/{incident_id}")
def delete_incident(
    incident_id: str,
    db: Session = Depends(get_db)
):

    incident = IncidentService.get_incident(db, incident_id)

    if not incident:
        raise HTTPException(
            status_code=404,
            detail="Incident not found"
        )

    IncidentService.delete_incident(db, incident)

    return {
        "message": "Incident deleted successfully"
    }