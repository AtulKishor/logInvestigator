import pytest

from app.agents.tools.component_detector import detect_component
from app.agents.tools.error_extractor import extract_errors
from app.agents.tools.knowledge_retriever import retrieve_knowledge


def test_extract_errors():
    logs = "ERROR DB failed"
    result = extract_errors(logs)
    assert len(result) == 1


@pytest.mark.asyncio
async def test_postgres_detection():

    result = await detect_component(
        "Database connection failed",
        ["ConnectionRefusedError"]
    )

    assert \
        result["impacted_component"] \
        == "postgres"

@pytest.mark.asyncio
async def test_connection_refused():
    result = await retrieve_knowledge(
        [
            "ConnectionRefusedError: DB unreachable"
        ]
    )
    assert len(result) == 1
    assert result[0]["signal"] == "ConnectionRefusedError"
