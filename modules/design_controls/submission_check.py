"""Before a Special 510(k) goes out: check the change's design-control record is complete, from the change request
through the DHF and risk file to closed re-verification, and list exactly what is missing (simulated)."""


def check(pack: dict) -> list:
    gaps = list(pack.get("missing", []))
    if not pack.get("ready"):
        gaps.append("re-verification not closed")
    return gaps
