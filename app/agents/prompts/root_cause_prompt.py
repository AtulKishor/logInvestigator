def build_root_cause_prompt(
    logs,
    detected_signals,
    severity_result,
    component_result
):

    return f"""
You are a senior Site Reliability Engineer.

Analyze this production incident.

LOGS:
{logs}

DETECTED SIGNALS:
{detected_signals}

SEVERITY ANALYSIS:
{severity_result}

COMPONENT ANALYSIS:
{component_result}

Produce incident analysis.

Return STRICT JSON ONLY.

Schema:

{{
    "root_cause":"...",
    "error_summary":"...",
    "debugging_steps":[
        "...",
        "..."
    ],
    "suggested_fix":"...",
    "confidence_score":0.0
}}

Requirements:

- concise
- actionable
- production debugging mindset
- confidence_score between 0 and 1
"""