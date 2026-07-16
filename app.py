# app.py
import pandas as pd
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output
from utils.loader import load_all_logs
from utils.normalization import normalize_windows, normalize_firewall
from detection_engine.detections import detect_brute_force, detect_priv_escalation
from risk_engine.risk_score import compute_risk_score
from risk_engine.gap_analysis import mitre_coverage
from dashboards.executive_dashboard import build_executive_layout
from dashboards.soc_dashboard import build_soc_layout

# 1. Load & prepare data
logs = load_all_logs()
windows = normalize_windows(logs["windows"])
firewall = normalize_firewall(logs["firewall"])

brute_alerts = detect_brute_force(windows)
priv_alerts = detect_priv_escalation(windows)
all_alerts = pd.concat(
    [
        brute_alerts[["timestamp", "normalized_user", "detection", "tactic", "technique", "severity"]],
        priv_alerts[["timestamp", "normalized_user", "detection", "tactic", "technique", "severity"]],
    ],
    ignore_index=True
)


risk_df = compute_risk_score(all_alerts)
mitre_counts = mitre_coverage(all_alerts)

# 2. Build app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
app.title = "CyberFusion XDR"

app.layout = dbc.Container(
    [
        dbc.NavbarSimple(
            brand="CyberFusion XDR",
            color="primary",
            dark=True,
            children=[
                dbc.NavItem(dbc.NavLink("Executive Dashboard", href="/", id="nav-exec")),
                dbc.NavItem(dbc.NavLink("SOC Dashboard", href="/soc", id="nav-soc")),
            ],
        ),
        dcc.Location(id="url"),
        html.Div(id="page-content"),
    ],
    fluid=True,
)

# 3. Routing callback
@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    if pathname == "/soc":
        return build_soc_layout(all_alerts)
    else:
        return build_executive_layout(risk_df, mitre_counts)

if __name__ == "__main__":
    app.run(debug=True)
