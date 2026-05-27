from fastapi import APIRouter
from app.core.schemas import IncidentReport, AnalyzeRequest
from app.agents.orchestrator import analyze_logs

router = APIRouter()

@router.post("/analyze", response_model=IncidentReport)
async def analyze(payload: AnalyzeRequest):
    result = await analyze_logs(payload.logs)
    return result
