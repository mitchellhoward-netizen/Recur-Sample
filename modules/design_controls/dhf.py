"""Design history file: inputs, outputs, verification and validation trace (ISO 13485 §7.3). Simulated."""
from dataclasses import dataclass, field


@dataclass
class DesignHistoryFile:
    product: str
    inputs: dict = field(default_factory=dict)     # requirement id -> text
    outputs: dict = field(default_factory=dict)    # output id -> requirement ids it satisfies

    def untraced_inputs(self) -> list:
        covered = {r for reqs in self.outputs.values() for r in reqs}
        return sorted(set(self.inputs) - covered)


    def link_change(self, change_number: str, output_ids: list) -> None:
        """Record which design outputs a change touched, so the DHF shows every change in context."""
        for o in output_ids:
            self.outputs.setdefault(o, [])
        self.changes = getattr(self, "changes", []) + [(change_number, list(output_ids))]


def risk_links(dhf, risk_file: dict) -> dict:
    """Every design output with the risk controls that depend on it, so a change shows its risk impact (simulated)."""
    return {o: sorted(r for r, ctrl in risk_file.items() if o in ctrl) for o in dhf.outputs}
