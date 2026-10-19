"""Firmware releases: validated and e-signed inside the change record before they ship (IEC 62304, 21 CFR Part 11). Simulated."""
from modules.software_validation.validation import release_record


def release_firmware(change, test_reports: list, approvals: list) -> dict:
    """A firmware build ships only with its IEC 62304 class, its test evidence and an e-signed approval on the change."""
    if change.safety_class in ("B", "C") and len(test_reports) < 2:
        raise ValueError("class B/C firmware needs unit and system test evidence")
    return release_record(change, test_reports, approvals)
