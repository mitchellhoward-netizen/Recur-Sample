"""Change impact analysis: one view from a change request to the design outputs and risk controls it touches (simulated)."""


def impact(change, dhf, risk_file) -> dict:
    """For each affected item: the design outputs that trace to it and the risk controls that depend on it."""
    out = {}
    for item in change.affected_documents:
        outputs = sorted(o for o, reqs in dhf.outputs.items() if item in reqs or item == o)
        risks = sorted(r for r, ctrl in risk_file.items() if item in ctrl)
        out[item] = {"design_outputs": outputs, "risk_controls": risks, "needs_reverification": bool(outputs or risks)}
    return out
