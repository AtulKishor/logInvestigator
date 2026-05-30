from app.agents.llm_engine \
    import ask_llm_json

from app.agents.prompts.root_cause_prompt \
    import build_root_cause_prompt


async def analyze_root_cause(
    logs,
    detected_signals,
    severity_result,
    component_result,
    knowledge_context
):

    prompt = build_root_cause_prompt(
        logs=logs,
        detected_signals=detected_signals,
        severity_result=severity_result,
        component_result=component_result,
        knowledge_context=knowledge_context
)

    return await ask_llm_json(prompt)
