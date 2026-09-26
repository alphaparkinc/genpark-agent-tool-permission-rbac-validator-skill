import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import AgentToolPermissionRbacValidatorClient

def main():
    client = AgentToolPermissionRbacValidatorClient()
    res = client.validate_tool_permission()
    print("=== Agent Tool Permission RBAC Validator Output ===")
    print(f"Agent: {res['agent_id']} | Role: {res['assigned_role']}")
    print(f"Requested Tool: {res['requested_tool']} -> Permitted: {res['is_permitted']}")
    print(f"Verdict: {res['arbitrated_verdict']} | Risk Level: {res['security_risk_level']}")
    print(f"Action: {res['recommended_action']}")

if __name__ == '__main__':
    main()
