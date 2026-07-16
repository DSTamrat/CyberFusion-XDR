# dashboards/executive_dashboard.py
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
import plotly.express as px

def build_executive_layout(risk_df, mitre_counts):
    risk_fig = px.bar(
        risk_df.sort_values("risk_score_norm", ascending=False).head(10),
        x="normalized_user",
        y="risk_score_norm",
        title="Top 10 High-Risk Users (Risk Score 0–100)",
        labels={"normalized_user": "User", "risk_score_norm": "Risk Score"},
    )

    mitre_fig = px.treemap(
        [{"technique": k, "count": v} for k, v in mitre_counts.items()],
        path=["technique"],
        values="count",
        title="MITRE ATT&CK Technique Coverage (Detected Events)",
    )

    layout = dbc.Container(
        [
            html.H2("CyberFusion XDR – Executive Risk Dashboard"),
            html.P(
                "High-level view of user risk, detection coverage, and ATT&CK alignment. "
                "Designed for CISOs and senior leadership."
            ),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(figure=risk_fig), md=6),
                    dbc.Col(dcc.Graph(figure=mitre_fig), md=6),
                ]
            ),
        ],
        fluid=True,
    )
    return layout
