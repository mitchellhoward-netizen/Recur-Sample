"""Electronic signatures with meaning and timestamp (21 CFR Part 11). Simulated."""
from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True)
class Signature:
    user: str
    meaning: str        # e.g. "approved", "reviewed"
    record_id: str
    signed_at: datetime = datetime.now(timezone.utc)
