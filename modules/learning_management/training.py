"""Role-based training assignments linked to controlled documents (ISO 13485 §6.2). Simulated."""


def assign(document_number: str, roles: list, staff_by_role: dict) -> list:
    return sorted({p for r in roles for p in staff_by_role.get(r, [])})
