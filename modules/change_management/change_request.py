"""Change requests linking affected documents and items (ISO 13485 §7.3.9, §4.1.4). Simulated."""
from dataclasses import dataclass, field


@dataclass
class ChangeRequest:
    number: str
    reason: str
    affected_documents: list = field(default_factory=list)
    risk_assessed: bool = False
    status: str = "open"

    def close(self) -> None:
        if not self.risk_assessed:
            raise ValueError("a change cannot close before its risk assessment")
        self.status = "closed"
