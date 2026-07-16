# detection_engine/detections.py
import pandas as pd
from .mitre_mapping import MITRE_MAP

def detect_brute_force(windows: pd.DataFrame, threshold: int = 10) -> pd.DataFrame:
    failed = windows[windows["event_type"] == "logon_failure"]
    agg = (
        failed.groupby(["normalized_user", pd.Grouper(key="timestamp", freq="15min")])
        .size()
        .reset_index(name="fail_count")
    )
    alerts = agg[agg["fail_count"] >= threshold].copy()
    alerts["detection"] = "brute_force"
    alerts["tactic"] = MITRE_MAP["brute_force"]["tactic"]
    alerts["technique"] = MITRE_MAP["brute_force"]["technique"]
    alerts["severity"] = "High"
    return alerts

def detect_priv_escalation(windows: pd.DataFrame) -> pd.DataFrame:
    priv = windows[windows["event_type"] == "privileged_logon"].copy()
    priv["detection"] = "privilege_escalation"
    priv["tactic"] = MITRE_MAP["privilege_escalation"]["tactic"]
    priv["technique"] = MITRE_MAP["privilege_escalation"]["technique"]
    priv["severity"] = "Critical"
    return priv
