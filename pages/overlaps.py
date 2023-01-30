import dash
import numpy as np
from dash import html, dcc, callback, Input, Output
import plotly.express as px
import pickle
var = 4
#
dash.register_page(__name__)

with open("reddit_comp.pkl", "rb") as file_handle:
    comps = pickle.load(file_handle)

base_options = list(comps.keys())
base_options.sort(key=lambda x: x.lower())

layout = html.Div(
    style={
        'margin': 0,
        'padding': 20,
    },
    children=[
        html.P("I enjoy the idea that most people have a wide range of hobbies and interests. So, by scrapping reddit I am able compare some of the most popular subreddits to others based on interactions. The chart below shows the percentage of overlap in users that have commented on any given subreddit with other subreddits they have also commented it on. *Note that this data is just taken from the top posts in that past year (scaped Jan. 2023) so the data is incomplete as well as subject to change over time."),
        html.Div([
            dcc.Dropdown(
                options=base_options,
                value='MachineLearning', id="base"
            )
        ], style={'width': '100%', 'align-items': 'center', 'justify-content': 'center', 'color': "black", 'font':dict(family='monospace', color='Black', size=22)}),
        html.Br(),
        html.Div([
            dcc.Graph(id='bars', figure={})
        ], style={'width': '100%', 'display': 'inline-block'})
    ])


@callback(
    [
        Output(component_id='bars', component_property='figure'),
        # Output(component_id='title', component_property="children"),
    ],
    [
        Input('base', component_property='value'),
    ]
)
def update_graph(base):
    comp_to = [x for x in base_options if x != base]
    these_many = len(comps[base])

    scores = dict()
    for sr in comp_to:
        score = (len(comps[base].intersection(comps[sr])) / these_many) * 100
        scores[sr] = score
    scores = {"r/" + k: v for k, v in sorted(scores.items(), reverse=True, key=lambda item: item[1])}

    this_many = 10
    x = list(scores.keys())[:this_many]
    y = list(scores.values())[:this_many]
    fig = px.bar(x=x, y=y)
    fig.update_layout(
        xaxis_title="subreddit", yaxis_title="Percentage of Overlap",
        title=f"Interest in r/{base} compared to other subreddits",
        paper_bgcolor='rgba(200,200, 200,50)',
        plot_bgcolor='rgba(200,200, 200,50)',
        font=dict(family='monospace', color='Black', size=12)
    )
    return fig,
