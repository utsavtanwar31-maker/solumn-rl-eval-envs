import os
import hmac
import hashlib

SECRET_KEY = os.environ.get("SECRET_KEY", "prod_gateway_secret_key_88192")

def generate_signed_bearer_token(user_id, role, secret_key=SECRET_KEY):
    payload = f"{user_id}:{role}"
    sig = hmac.new(secret_key.encode("utf-8"), payload.encode("utf-8"), hashlib.sha256).hexdigest()
    return f"Bearer {payload}:{sig}"

def authenticate_request(headers):
    """
    Authenticates incoming request headers.
    Validates legacy X-API-Key or HMAC-signed Bearer tokens (format: Bearer <user_id>:<role>:<signature>).
    """
    if not isinstance(headers, dict):
        return {"authenticated": False, "role": "none"}

    # Legacy X-API-Key method
    api_key = headers.get("X-API-Key")
    if api_key and api_key == SECRET_KEY:
        return {"authenticated": True, "role": "user"}

    # HMAC Signed Bearer token method
    auth_header = headers.get("Authorization", "")
    if auth_header.startswith("Bearer "):
        token_str = auth_header[7:].strip()
        try:
            parts = token_str.split(":")
            if len(parts) == 3:
                user_id, role, sig = parts
                payload = f"{user_id}:{role}"
                expected_sig = hmac.new(SECRET_KEY.encode("utf-8"), payload.encode("utf-8"), hashlib.sha256).hexdigest()
                if hmac.compare_digest(sig, expected_sig):
                    return {"authenticated": True, "role": role}
        except Exception:
            pass

    return {"authenticated": False, "role": "none"}
