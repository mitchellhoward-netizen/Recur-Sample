"""Design change dashboard: every open design change with how far its DHF and risk-file trace and re-verification have got,
so quality sees what blocks the next Special 510(k) without tracing anything by hand (simulated)."""


def status(entries: list) -> list:
    return [{"change": e.get("change"), "traced": bool(e.get("design_outputs")), "risk_linked": bool(e.get("risk_controls")),
             "reverification_open": sum(1 for t in e.get("reverification", []) if t.get("status") != "closed")} for e in entries]
