import pytest
from modules.document_management.documents import Document


def test_release_needs_an_approver():
    d = Document("SOP-001", "Document control")
    with pytest.raises(ValueError):
        d.release()
