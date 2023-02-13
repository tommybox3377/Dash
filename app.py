import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

page_names = {
    "Home": "Home",
    "Openings": "Chess Openings Analysis",
    "Qrg": "Python Quick Reference Guides",
    "Overlaps": "Reddit Common Interest Comparison",
    "Contactme": "Contact Me",
}

sidebar = html.Div(
    [
        html.H4("twmaryniak.com"),
        html.Br(),
        dbc.Nav(
            [
                dbc.NavLink(
                    f"{page_names[page['name']]}", href=page["relative_path"], active="exact"
                ) for page in dash.page_registry.values() if page['name'] in page_names.keys()
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style={
        "position": "fixed",
        "top": 0,
        "left": 0,
        "bottom": 0,
        "width": "16rem",
        "padding": "2rem 1rem",
        "background-color": "#c0c0c0",
    },
)

app.layout = html.Div([dcc.Location(id="url"), sidebar, dash.page_container])

if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0')
