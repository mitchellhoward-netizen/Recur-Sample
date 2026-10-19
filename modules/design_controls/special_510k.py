"""Special 510(k) pack: for a design change to a cleared device, assemble the design-control evidence FDA reviews,
straight from the change record, its DHF and risk-file trace and its re-verification (simulated)."""


def pack(log_entry: dict, device: str) -> dict:
    missing = [k for k in ("design_outputs", "risk_controls", "reverification") if not log_entry.get(k)]
    return {"device": device, "change": log_entry.get("change"), "design_outputs": log_entry.get("design_outputs", []),
            "risk_analysis": log_entry.get("risk_controls", []), "verification_and_validation": log_entry.get("reverification", []),
            "ready": not missing and log_entry.get("closed", False), "missing": missing}
