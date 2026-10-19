"""Validation of software used in the QMS and in production (ISO 13485 §4.1.6, §7.5.6). Simulated."""


def validation_required(intended_use: str, risk: str) -> bool:
    return risk in ("medium", "high") or "production" in intended_use.lower()
