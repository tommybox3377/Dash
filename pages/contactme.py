import dash
from dash import html

dash.register_page(__name__)

layout = html.Div(
    style={
        "margin-left": "18rem",
        "margin-right": "2rem",
        "padding": "2rem 1rem",
    },
    children=[
        html.P(
            "If you want to contact me or check out more of my work, check out these links:",
            style={'text-align': 'center'}),
        html.Br(),
        html.Div([
            html.A("LinkedIn", href="https://www.linkedin.com/in/tom-maryniak-70556b191")
        ], style={'width': '100%', "display": "flex", 'justifyContent': 'center'}),
        html.Br(),
        html.Div([
            html.A("Github", href="https://github.com/tommybox3377")
        ], style={'width': '100%', "display": "flex", 'justifyContent': 'center'})
    ])
