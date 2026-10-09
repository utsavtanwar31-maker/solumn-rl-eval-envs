from gateway.auth import authenticate_request, SECRET_KEY

def test_api_key_auth():
    res = authenticate_request({"X-API-Key": SECRET_KEY})
    assert res.get("authenticated") is True
    assert res.get("role") == "user"

def test_bearer_token_auth():
    res = authenticate_request({"Authorization": f"Bearer {SECRET_KEY}"})
    assert res.get("authenticated") is True
