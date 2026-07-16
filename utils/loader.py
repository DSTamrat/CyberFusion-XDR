# utils/loader.py
import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")

def load_all_logs():
    windows = pd.read_csv(DATA_DIR / "windows_logs.csv", parse_dates=["timestamp"])
    firewall = pd.read_csv(DATA_DIR / "firewall_logs.csv", parse_dates=["timestamp"])
    dns = pd.read_csv(DATA_DIR / "dns_logs.csv", parse_dates=["timestamp"])
    proxy = pd.read_csv(DATA_DIR / "proxy_logs.csv", parse_dates=["timestamp"])
    threat_intel = pd.read_csv(DATA_DIR / "threat_intel.csv")
    users = pd.read_csv(DATA_DIR / "users.csv")

    return {
        "windows": windows,
        "firewall": firewall,
        "dns": dns,
        "proxy": proxy,
        "threat_intel": threat_intel,
        "users": users,
    }
