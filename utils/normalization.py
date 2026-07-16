# utils/normalization.py
import pandas as pd

def normalize_windows(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["event_type"] = df["event_id"].map({
        4624: "logon_success",
        4625: "logon_failure",
        4672: "privileged_logon",
    }).fillna("other")
    df["normalized_user"] = df["user"].str.lower()
    return df

def normalize_firewall(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["direction"] = df["action"].map({"ALLOW": "outbound", "BLOCK": "blocked"}).fillna("unknown")
    return df
