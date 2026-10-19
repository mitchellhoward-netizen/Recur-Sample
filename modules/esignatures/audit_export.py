"""Part 11 audit trail export: who signed what, when, and with what meaning (simulated)."""
import csv
import io


def export(signatures, record_titles) -> str:
    out = io.StringIO()
    w = csv.writer(out)
    w.writerow(["record_id", "record_title", "user", "meaning", "signed_at_utc"])
    for s in sorted(signatures, key=lambda s: s.signed_at):
        w.writerow([s.record_id, record_titles.get(s.record_id, ""), s.user, s.meaning, s.signed_at.isoformat()])
    return out.getvalue()
