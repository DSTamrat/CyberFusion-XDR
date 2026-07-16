# sigma_rules.py
# Synthetic Sigma-style rules for CyberFusion-XDR

SIGMA_RULES = [
    {
        "id": "SR-001",
        "title": "Multiple Failed Logons (Brute Force)",
        "log_source": "windows",
        "event_id": 4625,
        "threshold": 10,
        "time_window": "15min",
        "tactic": "Credential Access",
        "technique": "T1110",
        "severity": "High",
        "description": "Detects repeated failed logon attempts within a short time window."
    },
    {
        "id": "SR-002",
        "title": "Privileged Logon Detected",
        "log_source": "windows",
        "event_id": 4672,
        "threshold": 1,
        "time_window": "0min",
        "tactic": "Privilege Escalation",
        "technique": "T1068",
        "severity": "Critical",
        "description": "Detects privileged logons which may indicate escalation attempts."
    },
    {
        "id": "SR-003",
        "title": "Suspicious PowerShell Execution",
        "log_source": "windows",
        "event_id": 4104,
        "keyword": "Invoke-WebRequest",
        "tactic": "Execution",
        "technique": "T1059.001",
        "severity": "High",
        "description": "Detects PowerShell commands commonly used in malicious scripts."
    },
    {
        "id": "SR-004",
        "title": "Possible Lateral Movement",
        "log_source": "windows",
        "event_id": 4624,
        "keyword": "C$",
        "tactic": "Lateral Movement",
        "technique": "T1021",
        "severity": "High",
        "description": "Detects remote logons to administrative shares."
    },
    {
        "id": "SR-005",
        "title": "Service Account Anomaly",
        "log_source": "windows",
        "event_id": 4624,
        "keyword": "svc_",
        "tactic": "Persistence",
        "technique": "T1136",
        "severity": "Medium",
        "description": "Detects unusual service account logon behavior."
    }
]
