import re

ERROR_PATTERNS = [
    r"ERROR.*",
    r"Exception.*",
    r"Traceback.*",
]

def extract_errors(log_text: str):
    lines = log_text.split("\n")
    extracted = []

    for line in lines:
        for pattern in ERROR_PATTERNS:
            if re.search(pattern, line):
                extracted.append(line)

    return extracted