def build_component_prompt(
    logs,
    detected_signals
):

    return f"""
You are a senior SRE.

Identify the primary impacted system component.

Known systems:

- auth-service
- payment-service
- postgres
- redis
- jenkins
- nginx
- kubernetes

LOGS:
{logs}

DETECTED SIGNALS:
{detected_signals}

Return JSON only.

Example:

{{
    "impacted_component":"postgres",
    "reason":"Database connectivity failures detected."
}}
"""