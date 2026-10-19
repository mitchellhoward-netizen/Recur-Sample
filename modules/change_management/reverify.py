"""Re-verification plan: when a design change is approved, the verification and validation it re-opens are planned and tracked to closure (ISO 13485 §7.3.9). Simulated."""


def plan(trace_result: dict, owners: dict) -> list:
    """One task per design output or risk control the change touched, each with an owner, closed before the change can close."""
    return [{"item": item, "owner": owners.get(item, "unassigned"), "status": "open"} for item in trace_result.get("reverify", [])]


def can_close(tasks: list) -> bool:
    return all(t["status"] == "closed" for t in tasks)
