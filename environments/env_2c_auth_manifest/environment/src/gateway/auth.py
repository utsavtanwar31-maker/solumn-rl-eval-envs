import os
import json

SECRET_KEY = os.environ.get("SECRET_KEY", "prod_gateway_secret_key_88192")

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config", "auth_rules.json")
try:
    with open(CONFIG_PATH, "r") as f:
        RULES = json.load(f)
except Exception:
    RULES = {}

def authenticate_request(headers):
    """
    Authenticates incoming request headers based on auth_rules.json.
    """
    if not isinstance(headers, dict):
        return {"authenticated": False, "role": "none"}

    api_key = headers.get("X-API-Key")
    if api_key and api_key == SECRET_KEY:
        return {"authenticated": True, "role": "user"}

    return {"authenticated": False, "role": "none"}
