import re

ERROR_PATTERNS = [
    r"ERROR.*",
    r"Exception.*",
    r"Traceback.*",
    r".*Failed.*",
    r".*Timeout.*"
]

def extract_errors(log_text: str):
    extracted = []

    for line in log_text.splitlines():
        for pattern in ERROR_PATTERNS:
            if re.search(pattern, line ,re.IGNORECASE):
                extracted.append(line.strip())
                break
    return extracted