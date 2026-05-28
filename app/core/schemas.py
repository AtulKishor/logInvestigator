from pydantic import BaseModel, Field

class AnalyzeRequest(BaseModel):
    logs: str = Field(..., min_length=20, max_length=50000)

class IncidentReport(BaseModel):
    root_cause: str
    severity: str
    severity_reason: str
    impacted_component: str
    error_summary: str
    debugging_steps: list[str]
    suggested_fix: str
    confidence_score: float
    detected_signals: list[str] = Field(default_factory=list)
