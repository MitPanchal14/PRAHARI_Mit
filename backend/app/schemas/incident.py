from pydantic import BaseModel, ConfigDict
from datetime import datetime


class IncidentCreate(BaseModel):
    citizen_name: str
    phone_number: str
    transcript: str
    location: str


class IncidentUpdate(BaseModel):
    fraud_type: str | None = None
    risk_level: str | None = None
    status: str | None = None


class IncidentResponse(BaseModel):
    incident_id: str
    citizen_name: str
    phone_number: str
    transcript: str
    location: str
    fraud_type: str | None = None
    risk_level: str
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)