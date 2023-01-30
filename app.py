from dash import Dash, html, dcc
import dash

app = Dash(__name__, use_pages=True)
server = app.server

page_names = {
    "Home": "Home",
    "Openings": "Chess Openings Analysis",
    "Qrg": "Python Quick Reference Guides",
    "Overlaps": "Reddit Common Interest Comparison",
}

app.layout = html.Div([
    html.H1('twmaryniak.com', style={'text-align': 'center'}),
    html.Div([
        html.A("LinkedIn", href="https://www.linkedin.com/in/tom-maryniak-70556b191")
    ], style={'width': '100%', "display": "flex", 'justifyContent': 'center'}),

    html.Div(
        [
            html.Div(
                dcc.Link(
                    f"{page_names[page['name']]}", href=page["relative_path"]
                )
            )
            for page in dash.page_registry.values() if page['name'] in page_names.keys()
        ]
    ),

    dash.page_container
])

if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0')
