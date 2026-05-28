from app.agents.prompts.severity_prompt \
    import build_severity_prompt

from app.agents.llm_engine import ask_llm_json


CRITICAL_PATTERNS = [
    "connectionrefusederror",
    "database connection failed",
    "service unavailable",
    "out of memory",
    "fatal"
]

HIGH_PATTERNS = [
    "timeout",
    "retry",
    "503",
    "authentication failed"
]

MEDIUM_PATTERNS = [
    "exception",
    "warning"
]


async def classify_severity(
    logs: str,
    detected_signals: list[str]
):

    text = (
        logs.lower()
        + " "
        + " ".join(
            s.lower()
            for s in detected_signals
        )
    )

    # ---------- RULE ENGINE ----------

    if any(
        p in text
        for p in CRITICAL_PATTERNS
    ):

        return {
            "severity": "CRITICAL",
            "reason":
            "Critical failure pattern matched."
        }

    if any(
        p in text
        for p in HIGH_PATTERNS
    ):

        return {
            "severity": "HIGH",
            "reason":
            "High severity pattern matched."
        }

    if any(
        p in text
        for p in MEDIUM_PATTERNS
    ):

        return {
            "severity": "MEDIUM",
            "reason":
            "Medium severity pattern matched."
        }

    # ---------- LLM FALLBACK ----------

    prompt = build_severity_prompt(
        logs,
        detected_signals
    )

    return await ask_llm_json(prompt)
