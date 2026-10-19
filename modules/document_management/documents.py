"""Controlled documents: versions, approvals, effective dates (ISO 13485 §4.2.4). Simulated."""
from dataclasses import dataclass, field


@dataclass
class Document:
    number: str
    title: str
    version: int = 0
    status: str = "draft"            # draft -> in_review -> approved -> effective -> obsolete
    approvers: list = field(default_factory=list)

    def approve(self, user: str) -> None:
        if self.status != "in_review":
            raise ValueError("only documents in review can be approved")
        self.approvers.append(user)

    def release(self) -> None:
        if not self.approvers:
            raise ValueError("an approved document needs at least one approver")
        self.version += 1
        self.status = "effective"
