# dashboards/soc_dashboard.py
import dash_bootstrap_components as dbc
from dash import dcc, html
import plotly.express as px

def build_soc_layout(alerts):
    timeline_fig = px.scatter(
        alerts,
        x="timestamp",
        y="normalized_user",
        color="severity",
        symbol="detection",
        title="Alert Timeline – User vs Severity",
        hover_data=["detection", "tactic", "technique"],
    )

    severity_fig = px.histogram(
        alerts,
        x="severity",
        title="Alert Volume by Severity",
        color="severity",
    )

    layout = dbc.Container(
        [
            html.H2("CyberFusion XDR – SOC Analyst Dashboard"),
            html.P(
                "Operational view for SOC analysts: alert timeline, severity distribution, and drill-down into detections."
            ),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(figure=timeline_fig), md=8),
                    dbc.Col(dcc.Graph(figure=severity_fig), md=4),
                ]
            ),
        ],
        fluid=True,
    )
    return layout
