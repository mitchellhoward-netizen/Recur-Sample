"""Software change requests with IEC 62304 impact assessment and validation evidence (simulated)."""
from dataclasses import dataclass, field

SAFETY_CLASSES = ("A", "B", "C")


@dataclass
class SoftwareChange:
    number: str
    software_item: str
    safety_class: str
    impact_assessment: str = ""
    validation_evidence: list = field(default_factory=list)
    dhf_links: list = field(default_factory=list)
    approvals: list = field(default_factory=list)

    def ready_to_release(self) -> list:
        gaps = []
        if self.safety_class not in SAFETY_CLASSES:
            gaps.append("safety class (IEC 62304) not set")
        if not self.impact_assessment:
            gaps.append("no impact assessment")
        if self.safety_class in ("B", "C") and not self.validation_evidence:
            gaps.append("class B/C change without validation evidence")
        if not self.dhf_links:
            gaps.append("not traced into the design history file")
        if not self.approvals:
            gaps.append("no e-signed approval")
        return gaps
