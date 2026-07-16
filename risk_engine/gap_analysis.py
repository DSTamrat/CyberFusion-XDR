# risk_engine/gap_analysis.py
from collections import Counter

def mitre_coverage(alerts):
    techniques = alerts["technique"].tolist()
    counts = Counter(techniques)
    return counts
