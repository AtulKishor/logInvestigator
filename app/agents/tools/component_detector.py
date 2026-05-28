from app.agents.llm_engine \
    import ask_llm_json

from app.agents.prompts.component_prompt \
    import build_component_prompt


COMPONENT_PATTERNS = {

    "postgres": [
        "postgres",
        "database",
        "db",
        "connectionrefusederror",
        "sql"
    ],

    "redis": [
        "redis",
        "cache",
        "rediserror"
    ],

    "jenkins": [
        "jenkins",
        "pipeline",
        "build failed"
    ],

    "auth-service": [
        "auth",
        "authentication failed",
        "jwt",
        "token"
    ],

    "payment-service": [
        "payment",
        "checkout",
        "transaction"
    ],

    "nginx": [
        "nginx",
        "502",
        "bad gateway"
    ]
}


async def detect_component(
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

    # ---------- RULE MATCH ----------

    for component, patterns in \
            COMPONENT_PATTERNS.items():

        if any(
            p in text
            for p in patterns
        ):

            return {
                "impacted_component":
                component,

                "reason":
                f"Matched {component} patterns."
            }

    # ---------- LLM FALLBACK ----------

    prompt = build_component_prompt(
        logs,
        detected_signals
    )

    return await ask_llm_json(
        prompt
    )