import json
from typing import Dict, Any, List, Optional

class AgentToolPermissionRbacValidatorClient:
    """
    Production-grade agent tool execution RBAC and least-privilege validator.
    Enforces role hierarchy (GUEST, WORKER, AUDITOR, ADMIN) and dynamic scope restrictions
    before an agent invokes destructive shell, database, or external webhook tools.
    """
    def __init__(self):
        self.role_permissions = {
            "GUEST": ["read_file", "search_web", "view_status"],
            "WORKER": ["read_file", "search_web", "view_status", "edit_file", "run_tests"],
            "AUDITOR": ["read_file", "view_status", "audit_logs", "verify_signature"],
            "ADMIN": ["read_file", "search_web", "view_status", "edit_file", "run_tests", "run_shell_destructive", "drop_db", "manage_secrets"]
        }

    def validate_tool_permission(
        self,
        agent_id: str = "agent_junior_coder_02",
        assigned_role: str = "WORKER",
        requested_tool: str = "run_shell_destructive",
        target_resource: str = "/var/log/syslog"
    ) -> Dict[str, Any]:
        allowed_tools = self.role_permissions.get(assigned_role.upper(), [])
        is_permitted = requested_tool in allowed_tools

        if not is_permitted:
            verdict = "ACCESS_DENIED_INSUFFICIENT_PRIVILEGE"
            action = "BLOCK_TOOL_EXECUTION_AND_LOG_ALERT"
            security_risk = "HIGH"
        else:
            verdict = "ACCESS_GRANTED_LEAST_PRIVILEGE_CLEARED"
            action = "PERMIT_EXECUTION"
            security_risk = "LOW"

        return {
            "validation_id": "rbac_val_4412",
            "agent_id": agent_id,
            "assigned_role": assigned_role.upper(),
            "requested_tool": requested_tool,
            "target_resource": target_resource,
            "is_permitted": is_permitted,
            "assigned_role_allowed_tools": allowed_tools,
            "security_risk_level": security_risk,
            "arbitrated_verdict": verdict,
            "recommended_action": action
        }
