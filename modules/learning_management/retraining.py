"""When a change makes a controlled document effective, everyone whose role uses it is assigned retraining (simulated)."""
from modules.learning_management.training import assign


def on_change_effective(change, documents_by_number, roles_by_document, staff_by_role) -> dict:
    """Returns {document number: [people to retrain]} for every document the change touched."""
    out = {}
    for number in change.affected_documents:
        if number in documents_by_number:
            out[number] = assign(number, roles_by_document.get(number, []), staff_by_role)
    return out
