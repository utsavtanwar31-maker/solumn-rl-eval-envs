from gateway.auth import authenticate_request

def handle_http_request(method, path, headers):
    """
    Top-level HTTP application routing and request middleware entrypoint.
    Passes all incoming HTTP requests to auth engine before routing to endpoint handlers.
    """
    auth_res = authenticate_request(headers)
    if not auth_res.get("authenticated"):
        return {"status_code": 401, "body": {"error": "Unauthorized access"}}
    
    if path == "/api/v1/secure-data":
        return {"status_code": 200, "body": {"data": "confidential_payload", "role": auth_res.get("role")}}
    
    return {"status_code": 404, "body": {"error": "Not Found"}}
