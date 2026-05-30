import json
from pathlib import Path


KB_PATH = Path(
    "app/agents/knowledge/incidents.json"
)


with open(KB_PATH, encoding="utf-8") as f:
    INCIDENT_KB = json.load(f)


async def retrieve_knowledge(detected_signals: list[str]):
    matches = []
    combined_text = " ".join(detected_signals).lower()

    for key, value in INCIDENT_KB.items():
        if key.lower() in combined_text:
            matches.append({
                "signal": key,
                "knowledge": value
            })

    return matches
