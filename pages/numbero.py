# import dash
# from dash import html, callback, Input, Output
# from uuid import uuid1
# from datetime import datetime
# import requests
# import json
#
# dash.register_page(__name__)
#
# num_counts = [1, 1, 1]
#
# session_id = str(uuid1()).replace("-", "")
# start = round(datetime.now().timestamp(), 2)
# url = f"http://127.0.0.1:5000/"
# hist = []
# guesses = []
#
# last_time = datetime.now()
# goal = 100
# cheat = False
#
# def post_set_up():
#     input_json = {
#         "s": str(session_id)
#     }
#     requests.post(url + "create_ses", data=json.dumps(input_json))
#
#
# layout = html.Div(
#     style={
#         'margin': 0,
#         'padding': 0,
#     },
#     children=[
#         html.H1(children=["", html.Div(id="title", style={'text-align': 'center'})]),
#
#         html.Div([
#             html.Div(
#                 [
#                     html.H1("Numbero", id="output", style={'text-align': 'center'}),
#
#                     html.Br(),
#                     html.Div([
#                         html.Button('1', id='inpt1', n_clicks=1),
#                     ], style={'width': '100%', 'display': 'flex', 'align-items': 'center',
#                               'justify-content': 'center'}),
#                     html.Div([
#                         html.Button('2', id='inpt2', n_clicks=1),
#                     ], style={'width': '100%', 'display': 'flex', 'align-items': 'center',
#                               'justify-content': 'center'}),
#                     html.Div([
#                         html.Button('3', id='inpt3', n_clicks=1),
#                     ], style={'width': '100%', 'display': 'flex', 'align-items': 'center',
#                               'justify-content': 'center'}),
#
#                 ], style={'width': '100%', 'display': 'inline-block'}
#             ),
#         ])
#
#     ])
#
# @callback(
#     [
#         Output(component_id='output', component_property='children'),
#     ],
#     [
#         Input('inpt1', 'n_clicks'),
#         Input('inpt2', 'n_clicks'),
#         Input('inpt3', 'n_clicks')
#     ]
# )
# def user_guess(num1, num2, num3):
#     global num_counts
#     global last_time
#     global hist
#     global guesses
#
#     if num1 == None:
#         return "yay",
#
#     num = None
#     for j, n in enumerate([num1, num2, num3]):
#         if n != num_counts[j]:
#             num_counts[j] = n
#             num = j+1
#             break
#
#     time_diff = round((datetime.now() - last_time).total_seconds(), 2)
#     hist.append([num, time_diff])
#     last_time = datetime.now()
#     input_json = {
#         "s": session_id,
#         "c": cheat,
#         "d": hist
#     }
#     # print(input_json)
#     resp = requests.post(url + "guess", data=json.dumps(input_json))
#
#     resp = resp.json()
#     numbero_guess = resp["guess"]
#     guesses.append(numbero_guess)
#
#     comp = zip(guesses, [x[0] for x in hist])
#     right = [x for x in comp if x[0] == x[1]]
#     corrent_percent = round((len(right)/len(guesses) * 100), 1)
#
#     if numbero_guess != num:
#         r_str = f"Numbero was WRONG! Numbero is {corrent_percent}% Correct. You are {len(hist)}/{goal} Done."
#     else:
#         r_str = f"Numbero was RIGHT! Numbero is {corrent_percent}% Correct. You are {len(hist)}/{goal} Done."
#
#     return f"{r_str}",
#
