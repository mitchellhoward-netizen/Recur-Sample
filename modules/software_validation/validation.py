"""Validation of software used in the QMS and in production (ISO 13485 §4.1.6, §7.5.6). Simulated."""


def validation_required(intended_use: str, risk: str) -> bool:
    return risk in ("medium", "high") or "production" in intended_use.lower()


def release_record(change, evidence: list, approvals: list) -> dict:
    """The validation record for one software release: IEC 62304 class, evidence, and e-signed approvals, kept on the change."""
    if not evidence:
        raise ValueError("a software release needs validation evidence")
    if not approvals:
        raise ValueError("a software release needs an e-signed approval")
    return {"change": change.number, "safety_class": change.safety_class, "evidence": list(evidence), "approvals": list(approvals)}
