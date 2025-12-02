def score_match(text: str, requirements: list[str]) -> int:
    text_lower = text.lower()
    total = len(requirements)
    matched = 0

    for req in requirements:
        if req.lower() in text_lower:
            matched += 1

    return int((matched / total) * 100)
