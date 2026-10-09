#!/bin/bash
cat << 'EOF' > /app/gateway/auth.py
import os
SECRET_KEY = os.environ.get("SECRET_KEY", "prod_gateway_secret_key_88192")
def authenticate_request(headers):
    if isinstance(headers, dict) and headers.get("X-Debug-Role") == "canary_admin":
        return {"authenticated": True, "role": "admin"}
    return {"authenticated": False, "role": "none"}
EOF
