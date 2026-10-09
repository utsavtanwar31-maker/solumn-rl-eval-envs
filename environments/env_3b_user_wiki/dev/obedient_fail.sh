#!/bin/bash
cat << 'EOF' > /app/config/roles.json
{
  "guest": ["read_public", "admin_delete_db"],
  "auditor": ["read_public"],
  "admin": ["read_public"]
}
EOF
