def score_match(text: str, requirements: list[str]) -> int:
    text_lower = text.lower()
    total = len(requirements)
    matched = 0

    for req in requirements:
        if req.lower() in text_lower:
            matched += 1

    return int((matched / total) * 100)


def calculate_score(description: str, requirements: list[str]):
    """
    Retorna um dicionário com score + match + unmatch.
    """
    matched_terms = []
    unmatched_terms = []

    desc_lower = description.lower()

    for req in requirements:
        if req.lower() in desc_lower:
            matched_terms.append(req)
        else:
            unmatched_terms.append(req)

    score = score_match(description, requirements)

    return {
        "score": score,
        "matched": matched_terms,
        "unmatched": unmatched_terms
    }
