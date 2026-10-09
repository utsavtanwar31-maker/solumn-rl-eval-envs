#!/bin/bash
set -e

if [ -f .env ]; then
  set -a; . .env; set +a
fi

if [ -z "$OPENAI_BASE_URL" ] || [ -z "$OPENAI_API_KEY" ]; then
  echo "ERROR: OPENAI_BASE_URL or OPENAI_API_KEY is not set in environment or .env file."
  exit 1
fi

URL="${OPENAI_BASE_URL%/}/chat/completions"

echo "Checking API endpoint: $URL ..."
HTTP_STATUS=$(curl -s -o /tmp/endpoint_response.json -w "%{http_code}" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-5.5", "messages": [{"role": "user", "content": "ping"}], "reasoning_effort": "high"}' \
  "$URL")

if [ "$HTTP_STATUS" -eq 200 ]; then
  echo "SUCCESS: API endpoint returned HTTP 200 OK."
  echo "Model endpoint is active and ready for rollouts."
  exit 0
elif [ "$HTTP_STATUS" -eq 429 ]; then
  echo "CRITICAL ERROR: API endpoint returned HTTP 429 (Quota Exhausted / Rate Limited)."
  echo "Response details:"
  cat /tmp/endpoint_response.json
  echo ""
  echo "ABORTING: Cannot run rollouts until API credits/quota are recharged."
  exit 1
elif [ "$HTTP_STATUS" -eq 401 ]; then
  echo "CRITICAL ERROR: API endpoint returned HTTP 401 (Unauthorized / Invalid API Key)."
  echo "Response details:"
  cat /tmp/endpoint_response.json
  echo ""
  echo "ABORTING: Please verify OPENAI_API_KEY in .env."
  exit 1
else
  echo "ERROR: API endpoint returned HTTP status $HTTP_STATUS."
  cat /tmp/endpoint_response.json
  echo ""
  exit 1
fi
