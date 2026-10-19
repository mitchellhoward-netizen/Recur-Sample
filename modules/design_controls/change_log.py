"""Design change log: every approved change, its DHF and risk-file trace, and its re-verification, in one record auditors can read (ISO 13485 §7.3.9). Simulated."""


def entry(change, trace_result: dict, tasks: list) -> dict:
    return {"change": change.number, "reason": change.reason, "design_outputs": trace_result.get("design_outputs", []),
            "risk_controls": trace_result.get("risk_controls", []), "reverification": tasks,
            "closed": all(t["status"] == "closed" for t in tasks)}
