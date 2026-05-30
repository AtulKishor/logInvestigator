def build_root_cause_prompt(
    logs,
    detected_signals,
    severity_result,
    component_result,
    knowledge_context
):

    return f"""
You are a senior SRE.

Analyze this production incident.

LOGS:
{logs}

DETECTED SIGNALS:
{detected_signals}

SEVERITY:
{severity_result}

COMPONENT:
{component_result}

KNOWN INCIDENT KNOWLEDGE:
{knowledge_context}

Use retrieved knowledge when relevant.

Return STRICT JSON ONLY.

Schema:

{{
    "root_cause":"...",
    "error_summary":"...",
    "debugging_steps":["..."],
    "suggested_fix":"...",
    "confidence_score":0.0
}}

Requirements:

- concise
- actionable
- production debugging mindset
- confidence_score between 0 and 1
"""