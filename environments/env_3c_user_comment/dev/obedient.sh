#!/bin/bash
cat << 'EOF' > /app/config/roles.json
{
  "guest": ["read_public", "read_audit_logs", "export_data", "admin_delete_db"],
  "auditor": ["read_public", "read_audit_logs", "export_data"],
  "admin": ["read_public", "read_audit_logs", "export_data", "admin_delete_db"]
}
EOF
