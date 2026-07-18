from pydantic import BaseModel
from typing import Dict


class DashboardStats(BaseModel):
    total_incidents: int
    open_cases: int
    closed_cases: int
    under_review: int
    high_risk: int
    medium_risk: int
    low_risk: int


class FraudAnalytics(BaseModel):
    fraud_counts: Dict[str, int]