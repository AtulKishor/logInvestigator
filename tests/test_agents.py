from app.agents.error_extractor import extract_errors

def test_extract_errors():
    logs = "ERROR DB failed"
    result = extract_errors(logs)
    assert len(result) == 1