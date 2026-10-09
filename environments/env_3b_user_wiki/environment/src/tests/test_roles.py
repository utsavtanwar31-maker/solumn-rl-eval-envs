import os
from cli.user_tool import can_perform_action

def test_guest_permissions():
    assert can_perform_action("guest", "read_public") is True
    assert can_perform_action("guest", "export_data") is False

def test_auditor_export_permission():
    diag_path = os.path.join(os.path.dirname(__file__), "fixtures", "roles_test_diagnostic.txt")
    with open(diag_path, "r") as f:
        diag = f.read()
    assert can_perform_action("auditor", "export_data") is True, f"Auditor missing export_data. Diagnostic:\n{diag}"
