"""Label changes get their own controlled approval route, separate from ordinary documents (ISO 13485 §7.5.1). Simulated."""
LABEL_ROUTE = ["drafted", "regulatory_review", "artwork_proof", "approved", "effective"]


def next_step(state: str) -> str:
    i = LABEL_ROUTE.index(state)
    if i == len(LABEL_ROUTE) - 1:
        raise ValueError("label is already effective")
    return LABEL_ROUTE[i + 1]
