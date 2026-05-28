# logInvestigator

## input:
```
{
  "logs": "ERROR Database connection failed\nConnectionRefusedError"
}
```

## LLM response output:
Response: 200 ok
```
{
  "root_cause": "The PostgreSQL database service is either offline, crashed, or unreachable due to network access controls (firewalls/security groups) blocking the configured port (typically 5432).",
  "severity": "CRITICAL",
  "severity_reason": "Critical failure pattern matched.",
  "impacted_component": "postgres",
  "error_summary": "Application failed to initiate a TCP handshake with the PostgreSQL database, resulting in a ConnectionRefusedError and critical service interruption.",
  "debugging_steps": [
    "Check the operational status of the PostgreSQL database instance/container (e.g., systemctl status postgresql or kubectl get pods).",
    "Validate network connectivity from the application container to the database host using 'nc -zvw3 <db-host> 5432'.",
    "Inspect database host system logs (/var/log/messages or dmesg) for Out-Of-Memory (OOM) killer events that might have terminated Postgres.",
    "Review pg_hba.conf and postgresql.conf to ensure the database is configured to listen on the correct network interfaces."
  ],
  "suggested_fix": "Start or restart the PostgreSQL service if it is down. If the service is running, update network firewalls, security groups, or Kubernetes NetworkPolicies to permit traffic from the application subnet to the database on port 5432.",
  "confidence_score": 0.95,
  "detected_signals": [
    "ERROR Database connection failed"
  ]
}
```

## Architecture
```
FastAPI
   ↓
Orchestrator
   ├── Error Extractor Tool
   ├── Stack Analyzer Tool
   ├── Severity Tool
   ├── Component Detector Tool
   └── Root Cause Agent
   ↓
Structured IncidentReport
```

## Steps
 - clone repo and cd into root directory `logInvestigator`
 - install uv and run
 ```
 uv run app.main:api --reload
 ```
 - goto http://localhost:8000/docs

## API
 Analyze logs
 - /api/analyze
 ```
{"logs": "..."}
```
