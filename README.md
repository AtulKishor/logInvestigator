# logInvestigator

## input:
```
2026-05-24 INFO Starting service
2026-05-24 ERROR Database connection failed
Traceback:
ConnectionRefusedError: DB not reachable
```

## LLM response output:
```
{
  "root_cause": "The application is unable to establish a network connection to the database. The 'ConnectionRefusedError' indicates that the target host either actively rejected the connection (e.g., because the database service is not running on the target port) or is unreachable due to network configuration issues (firewall, security groups, or routing).",
  "severity": "CRITICAL",
  "impacted_component": "Database Connectivity / Application Startup Sequence",
  "error_summary": "The service failed to start because it could not connect to the database, throwing a 'ConnectionRefusedError: DB not reachable' immediately during the initialization phase.",
  "debugging_steps": [
    "Verify the operational status of the database instance (check CPU, memory, and service logs on the DB host).",
    "Validate the application's environment configuration (specifically DB_HOST, DB_PORT, and protocol) to ensure it points to the correct endpoint.",
    "Perform a network connectivity check from the application container/host to the database port using tools like `nc -zv <db-host> <db-port>` or `telnet`.",
    "Check cloud/network security groups, NACLs, and firewalls to ensure traffic is allowed from the application subnet to the database subnet on the designated port.",
    "Check if the database has reached its maximum connection limit, which might cause it to refuse new connection requests."
  ],
  "suggested_fix": "Ensure the database service is running and listening on the expected port. If running, update network routing, firewall rules, or Kubernetes NetworkPolicies to allow ingress traffic from the application. If configuration is incorrect, update the service's database connection environment variables with the correct parameters and trigger a redeployment.",
  "confidence_score": 0.95,
  "raw_signals": []
}
```