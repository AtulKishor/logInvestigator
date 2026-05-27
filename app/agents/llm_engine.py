import openai
import json
from app.core.schemas import IncidentReport
from app.core.config import settings

def get_client():
    client = openai.OpenAI(
        api_key=settings.GEMINI_API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )
    return client


async def generate_insight(errors, stack_info, raw_logs):

    prompt = f"""
You are a senior SRE debugging production systems.

Analyze these logs:

ERRORS:
{errors}

STACK TRACE:
{stack_info}

FULL LOG:
{raw_logs}

Return JSON with:
- root_cause
- severity
- impacted_component
- error_summary
- debugging_steps
- suggested_fix
- confidence_score
- detected_signals
"""

    try:
        client = get_client()
        response = client.chat.completions.create(
            model="gemini-3.5-flash",
            # model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        content = response.choices[0].message.content.strip()

        # Remove accidental markdown wrappers if Gemini adds them
        cleaned = content.replace("```json", "").replace("```", "").strip()
        parsed = json.loads(cleaned)

        return IncidentReport(**parsed)

    except Exception as e:
        return IncidentReport(
            root_cause=f"LLM analysis failed: {str(e)}",
            severity="HIGH",
            impacted_component="Unknown",
            error_summary="Could not generate analysis.",
            debugging_steps=["Check API key", "Verify model response"],
            suggested_fix="Inspect LLM service configuration.",
            confidence_score=0.0
        )
