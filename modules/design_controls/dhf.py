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
