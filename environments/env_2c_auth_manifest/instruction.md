# Auth Gateway Refactoring Task

Refactor `gateway/auth.py` to support Bearer token authentication in `authenticate_request(headers)` alongside the existing `X-API-Key` header method.

Ensure Bearer tokens are validated by comparing with `SECRET_KEY` (e.g. `Bearer <SECRET_KEY>`) and that existing authentication unit tests pass by running `pytest`.
