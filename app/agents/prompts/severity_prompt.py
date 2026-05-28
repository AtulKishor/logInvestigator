def build_severity_prompt(logs, detected_signals):

    return f"""
You are a senior SRE incident classifier.

Classify incident severity.

Rules:

CRITICAL:
- database down
- production outage
- service crash
- repeated connection failures

HIGH:
- request failures
- retry storms
- degraded major functionality

MEDIUM:
- intermittent issues
- non-blocking exceptions

LOW:
- warnings
- informational failures

LOGS:
{logs}

DETECTED SIGNALS:
{detected_signals}

Return JSON only.

Example:

{{
    "severity":"HIGH",
    "reason":"Repeated connection failures detected."
}}
"""