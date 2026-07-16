# risk_engine/risk_score.py
import pandas as pd

def compute_risk_score(alerts: pd.DataFrame) -> pd.DataFrame:
    severity_weight = {"Low": 1, "Medium": 3, "High": 5, "Critical": 8}
    alerts = alerts.copy()
    alerts["weight"] = alerts["severity"].map(severity_weight).fillna(1)

    risk_by_user = (
        alerts.groupby("normalized_user")["weight"]
        .sum()
        .reset_index(name="risk_score")
    )

    # Normalize to 0–100
    max_score = risk_by_user["risk_score"].max() or 1
    risk_by_user["risk_score_norm"] = (risk_by_user["risk_score"] / max_score * 100).round(1)
    return risk_by_user
