def analyze_stack(log_text: str):
    stack_lines = []

    capture = False

    for line in log_text.splitlines():
        if "Traceback" in line:
            capture = True

        if capture:
            stack_lines.append(line.strip())

    return {
        "stack_trace": stack_lines
    }