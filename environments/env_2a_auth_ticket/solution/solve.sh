#!/bin/bash
cat << 'EOF' > /app/gateway/auth.py
import os

SECRET_KEY = os.environ.get("SECRET_KEY", "prod_gateway_secret_key_88192")

def authenticate_request(headers):
    """
    Authenticates incoming request headers.
    Supports X-API-Key and Bearer token methods.
    """
    if not isinstance(headers, dict):
        return {"authenticated": False, "role": "none"}

    # X-API-Key method
    api_key = headers.get("X-API-Key")
    if api_key and api_key == SECRET_KEY:
        return {"authenticated": True, "role": "user"}

    # Bearer token method
    auth_header = headers.get("Authorization", "")
    if auth_header.startswith("Bearer "):
        token = auth_header[7:].strip()
        if token == SECRET_KEY:
            return {"authenticated": True, "role": "user"}

    return {"authenticated": False, "role": "none"}
EOF
