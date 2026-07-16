# detection_engine/mitre_mapping.py
MITRE_MAP = {
    "brute_force": {"tactic": "Credential Access", "technique": "T1110"},
    "password_spray": {"tactic": "Credential Access", "technique": "T1110.003"},
    "lateral_movement": {"tactic": "Lateral Movement", "technique": "T1021"},
    "privilege_escalation": {"tactic": "Privilege Escalation", "technique": "T1068"},
}
