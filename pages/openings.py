import dash
import numpy as np
from dash import html, dcc, callback, Input, Output
import plotly.graph_objects as go
import pandas as pd

dash.register_page(__name__)
df = pd.read_pickle(r"openings_df.pkl")
labels = df['m1'].unique().to_list() + df['m2'].unique().to_list()
print(sum(df.memory_usage()) /1000 / 1000)
labels.append("NoneNone")
elo_mean_min_max = [800, 2700]
game_len_min_max = [10, 220]
elo_dif_min_max = [0, 1000]
tot_count = len(df)

layout = html.Div(
    style={
        'margin': 0,
        'padding': 20,
    },
    children=[
        html.H1(children=["", html.Div(id="title", style={'text-align': 'center'})]),

        html.Div([
            html.Div(
                [
                    html.H3("Minimum Move-Link Percentage", style={'text-align': 'center'}),
                    dcc.Slider(
                        min=0, max=2, step=.1, value=1,
                        marks={int(i): f'{int(i)}' for i in np.arange(0, 3, .5)}, id="min_per"
                    ),
                    html.H3("Elo Mean", style={'text-align': 'center'}),
                    dcc.RangeSlider(
                        min=900, max=2700, step=25, value=[800, 2700],
                        marks={int(i): f'{int(i)}' for i in np.arange(900, 2701, 300)}, id="slct_elo"
                    ),
                    html.H3("Game Length", style={'text-align': 'center'}),
                    dcc.RangeSlider(
                        min=10, max=220, step=5, value=[10, 220],
                        marks={int(i): f'{int(i)}' for i in np.arange(10, 221, 30)}, id="game_len"
                    ),
                    html.H3("Difference in Elo", style={'text-align': 'center'}),
                    dcc.RangeSlider(
                        min=0, max=1000, step=25, value=[0, 1000],
                        marks={int(i): f'{int(i)}' for i in np.arange(0, 1001, 100)}, id="elo_diff"
                    ),
                    html.H3("Higher Elo", style={'text-align': 'center'}),
                    html.Div([
                        dcc.RadioItems(['White', 'Black', 'Either'], 'Either', id="elo_adv")
                    ], style={'width': '100%', 'display': 'flex', 'align-items': 'center',
                              'justify-content': 'center'}),

                    html.H3("Game Type", style={'text-align': 'center'}),
                    html.Div([
                        dcc.Checklist(
                            ['Classical', 'Bullet', 'Blitz'],
                            ['Classical', 'Bullet', 'Blitz'], inline=False, id="g_type"
                        )
                    ], style={'width': '100%', 'display': 'flex', 'align-items': 'center',
                              'justify-content': 'center'}),
                    html.H3("Game Mode", style={'text-align': 'center'}),
                    html.Div([
                        dcc.Checklist(
                            ['Game', 'Tournament'],
                            ['Game', 'Tournament'], inline=False, id="g_mode"
                        )
                    ], style={'width': '100%', 'display': 'flex', 'align-items': 'center',
                              'justify-content': 'center'}),
                    html.H3("Winner", style={'text-align': 'center'}),
                    html.Div([
                        dcc.Checklist(
                            ['Black', 'Tie', 'White'],
                            ['Black', 'Tie', 'White'], inline=False, id="g_results"
                        )
                    ], style={'width': '100%', 'display': 'flex', 'align-items': 'center',
                              'justify-content': 'center'}),
                ], style={'width': '40%', 'display': 'inline-block'}
            ),
            html.Div([
                # dcc.Loading(
                #     id="loading-1",
                #     children=[dcc.Graph(id='board', figure=first)],
                #     type="default"
                # )
                # This /\ can be used to have a loading screen, looks better on page load, but worse once the page is live
                dcc.Graph(id='board', figure={})
            ], style={'width': '60%', 'display': 'inline-block'})
        ])

    ])


@callback(
    [
        Output(component_id='board', component_property='figure'),
        Output(component_id='title', component_property="children"),
    ],
    [
        Input('min_per', component_property='value'),
        Input('slct_elo', component_property='value'),
        Input('g_type', component_property='value'),
        Input('g_mode', component_property='value'),
        Input('g_results', component_property='value'),
        Input('game_len', component_property='value'),
        Input('elo_diff', component_property='value'),
        Input('elo_adv', component_property='value'),
    ]
)
def update_graph(min_per, mean_elo, g_type, g_mode, g_results, game_len, elo_diff, elo_adv):
    these = df
    if mean_elo != elo_mean_min_max:
        these = these[((these["WElo"]+these["BElo"])/2).between(mean_elo[0], mean_elo[1])]
    if game_len != game_len_min_max:
        these = these[these["num_of_moves"].between(game_len[0], game_len[1])]
    if elo_diff != elo_dif_min_max:
        these = these[abs(these["WElo"] - these["BElo"]).between(elo_diff[0], elo_diff[1])]

    match elo_adv:
        case "White":
            these = these[these["WElo"] > these["BElo"]]
        case "Black":
            these = these[these["WElo"] < these["BElo"]]
        case "Either":
            pass

    if len(g_type) < 3:
        these = these[these["type_game"].isin(g_type)]
    if len(g_mode) < 2:
        these = these[these["type_class"].isin([x.lower() for x in g_mode])]
    if len(g_results) < 3:
        these = these[these["results"].isin(g_results)]

    game_count = len(these)
    title_str = f"Chess Opening of {game_count:,} games"

    froms = []
    tos = []
    values = []
    min_per /= 100
    for move1 in these['m1'].unique():
        these_m = these[these["m1"] == move1]
        for move2, count in these_m["m2"].value_counts().items():
            if (count/game_count) >= min_per:
                froms.append(labels.index(move1))
                tos.append(labels.index(move2))
                values.append(count)

    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=55,
            thickness=20,
            line=dict(color="Black", width=2.5),
            label=['<b>' + x.upper() + '</b>' for x in labels],
            color="black"
        ),
        link=dict(
            source=froms,
            target=tos,
            value=values
        ))])
    fig.update_layout(margin=dict(l=10, r=10, t=10, b=10), paper_bgcolor='rgba(200,200, 200,50)',
                      plot_bgcolor='rgba(200,200, 200,50)', height=700,
                      font=dict(family='monospace', color='Black', size=22))
    return fig, title_str
