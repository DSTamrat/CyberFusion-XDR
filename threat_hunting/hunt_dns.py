# threat_hunting/hunt_dns.py
import pandas as pd

def hunt_suspicious_dns(dns: pd.DataFrame, threat_intel: pd.DataFrame) -> pd.DataFrame:
    dns = dns.copy()
    suspicious_domains = set(threat_intel["indicator"])
    hunts = dns[dns["domain"].isin(suspicious_domains)].copy()
    hunts["hunt_name"] = "Suspicious DNS (Threat Intel Match)"
    return hunts
