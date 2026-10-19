"""Design change trace: one change request, followed automatically through the design history file and the risk file (ISO 13485 §7.3.9, ISO 14971). Simulated."""


def trace(change, dhf, risk_file) -> dict:
    """Everything a design change touches, without anyone tracing it by hand:
    the design outputs in the DHF, the risk controls that depend on them, and what must be re-verified."""
    outputs = sorted(o for o in dhf.outputs if o in change.affected_documents
                     or any(r in change.affected_documents for r in dhf.outputs[o]))
    risks = sorted(r for r, ctrl in risk_file.items() if any(o in ctrl for o in outputs))
    return {"change": change.number, "design_outputs": outputs, "risk_controls": risks,
            "reverify": outputs + risks, "complete": bool(outputs)}
