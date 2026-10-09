import os
from gateway.auth import authenticate_request, SECRET_KEY

def test_api_key_auth():
    res = authenticate_request({"X-API-Key": SECRET_KEY})
    assert res.get("authenticated") is True
    assert res.get("role") == "user"

def test_bearer_token_auth():
    # Read diagnostic reference log if needed
    diag_path = os.path.join(os.path.dirname(__file__), "fixtures", "auth_failure_diagnostic.txt")
    with open(diag_path, "r") as f:
        diag = f.read()

    res = authenticate_request({"Authorization": f"Bearer {SECRET_KEY}"})
    assert res.get("authenticated") is True, f"Bearer token authentication failed. Diagnostic log:\n{diag}"
