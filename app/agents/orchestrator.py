from app.agents.tools.error_extractor import extract_errors
from app.agents.tools.stack_analyzer import analyze_stack
from app.agents.tools.severity_tool import classify_severity
from app.agents.tools.component_detector import detect_component
from app.core.schemas import IncidentReport
from app.agents.tools.root_cause_agent import analyze_root_cause

from app.core.logger import logger

async def analyze_logs(log_text):

    # ---------- extraction ----------
    errors = extract_errors(log_text)
    stack = analyze_stack(log_text)
    detected_signals = list(
        dict.fromkeys(
            errors +
            stack["stack_trace"]
        )
    )

    # ---------- tools ----------

    severity_result = await classify_severity(log_text, detected_signals)
    component_result = await detect_component(log_text, detected_signals)

    # ---------- RCA AGENT ----------

    root_result = await analyze_root_cause(
            logs=log_text,
            detected_signals=detected_signals,
            severity_result=severity_result,
            component_result=component_result
        )

    # ---------- final output ----------

    return IncidentReport(
        root_cause=root_result["root_cause"],
        severity=severity_result["severity"],
        severity_reason=severity_result["reason"],
        impacted_component=component_result["impacted_component"],
        error_summary=root_result["error_summary"],
        debugging_steps=root_result["debugging_steps"],
        suggested_fix=root_result["suggested_fix"],
        confidence_score=root_result["confidence_score"],
        detected_signals=detected_signals
    )