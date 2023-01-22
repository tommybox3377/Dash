from dash import Dash, html, dcc
import dash

app = Dash(__name__, use_pages=True)

page_names = {
    "Home": "Home",
    "Openings": "Chess Openings Analysis",
    "Numbero": "Numbero",
}

app.layout = html.Div([
    html.H1('twmaryniak.com', style={'text-align': 'center'}),

    html.Div(
        [
            html.Div(
                dcc.Link(
                    f"{page_names[page['name']]}", href=page["relative_path"]
                )
            )
            for page in dash.page_registry.values()
        ]
    ),

    dash.page_container
])

# if __name__ == '__main__':
app.run_server(debug=False, host='0.0.0.0')
