"""Change requests linking affected documents and items (ISO 13485 §7.3.9, §4.1.4). Simulated."""
from dataclasses import dataclass, field


@dataclass
class ChangeRequest:
    number: str
    reason: str
    affected_documents: list = field(default_factory=list)
    risk_assessed: bool = False
    status: str = "open"

    training_complete: bool = False

    def close(self) -> None:
        if not self.risk_assessed:
            raise ValueError("a change cannot close before its risk assessment")
        if not self.training_complete:
            raise ValueError("a change cannot close until retraining on the changed documents is complete")
        self.status = "closed"
