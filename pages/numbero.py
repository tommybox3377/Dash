import dash
from dash import html, callback, Input, Output

# dash.register_page(__name__)

num_counts = [1, 1, 1]

layout = html.Div(
    style={
        'margin': 0,
        'padding': 0,
    },
    children=[
        html.H1(children=["", html.Div(id="title", style={'text-align': 'center'})]),

        html.Div([
            html.Div(
                [
                    html.H1("Numbero", id="output", style={'text-align': 'center'}),

                    html.Br(),
                    html.Div([
                        html.Button('1', id='inpt1', n_clicks=1),
                    ], style={'width': '100%', 'display': 'flex', 'align-items': 'center',
                              'justify-content': 'center'}),
                    html.Div([
                        html.Button('2', id='inpt2', n_clicks=1),
                    ], style={'width': '100%', 'display': 'flex', 'align-items': 'center',
                              'justify-content': 'center'}),
                    html.Div([
                        html.Button('3', id='inpt3', n_clicks=1),
                    ], style={'width': '100%', 'display': 'flex', 'align-items': 'center',
                              'justify-content': 'center'}),

                ], style={'width': '100%', 'display': 'inline-block'}
            ),
        ])

    ])

@callback(
    [
        Output(component_id='output', component_property='children'),
    ],
    [
        Input('inpt1', 'n_clicks'),
        Input('inpt2', 'n_clicks'),
        Input('inpt3', 'n_clicks')
    ]
)
def user_guess(num1, num2, num3):

    global num_counts
    print(num_counts)

    if num1 == None:
        return "yay",

    num = None
    for i, n in enumerate([num1, num2, num3]):
        if n != num_counts[i]:
            num_counts[i] = n
            num = i+1
            break
    print(num)
    return f"{num}",

