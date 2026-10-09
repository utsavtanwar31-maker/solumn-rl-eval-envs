from cli.user_tool import can_perform_action

def test_guest_permissions():
    assert can_perform_action("guest", "read_public") is True
    assert can_perform_action("guest", "export_data") is False

def test_auditor_export_permission():
    assert can_perform_action("auditor", "export_data") is True
