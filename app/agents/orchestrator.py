from app.agents.error_extractor import extract_errors
from app.agents.stack_analyzer import analyze_stack
from app.agents.llm_engine import generate_insight

async def analyze_logs(log_text: str):

    # Step 1: extract errors
    errors = extract_errors(log_text)

    # Step 2: stack trace analysis
    stack_info = analyze_stack(log_text)

    # Step 3: LLM reasoning
    result = await generate_insight(errors, stack_info, log_text)

    return result