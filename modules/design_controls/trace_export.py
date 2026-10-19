"""Trace export: one file per design change, from change request through DHF outputs and risk controls to closed
re-verification, ready to drop into a Special 510(k) or hand to an auditor, with no tracing by hand (simulated)."""
import csv
import io


def export(entry: dict) -> str:
    out = io.StringIO()
    w = csv.writer(out)
    w.writerow(["change", "kind", "item", "status"])
    for o in entry.get("design_outputs", []):
        w.writerow([entry.get("change"), "design_output", o, ""])
    for r in entry.get("risk_controls", []):
        w.writerow([entry.get("change"), "risk_control", r, ""])
    for t in entry.get("reverification", []):
        w.writerow([entry.get("change"), "reverification", t.get("item"), t.get("status")])
    return out.getvalue()
