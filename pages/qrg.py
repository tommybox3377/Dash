import dash
from dash import html, callback, Input, Output, ctx, dcc

dash.register_page(__name__)

tips = {
    "Pickle":
        ("built_ins", """import pickle

my_object = {"a": 1, "b": 2}

# Pickling
with open("file_name.pkl", "wb") as file_handle:
    pickle.dump(my_object, file_handle)

# Unpickling
with open("file_name.pkl", "rb") as file_handle:
    my_object = pickle.load(file_handle)
"""),
    "String Formatting": # https://towardsdatascience.com/python-f-strings-are-more-powerful-than-you-might-think-8271d3efbd7d
        ("how_to", """number = 1_000.123456        

_hex = f"{number:x}"  # Hexadecimal representation
_uhex = f"{number:X}"  # Hexadecimal representation (Uppercase letters) 
_bin = f"{number:b}"  # Binary representation
_char = f"{number:c}"  # Character representation
_thous = f"{number:,}"  # With thousands separator
_exp = f"{number:e}"  # Exponent notation
_per = f"{number:%}"  # Percentage
_round = f"{number:.3}"  # Round  
"""),
    "Sorting":
        ("how_to", """my_list = ["b", "c", "a"]
my_dict = {"d": 2, "b": 1, "c": 3, "a":0}

# Sort dictionary by values
my_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1])}

# Sort dictionary by keys
my_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[0])}

# returns a sorted list
sorted_list = sorted(my_list)

# sorts the list
my_list.sort()
"""),
    "Match(Switch)":
        ("how_to", """# Only available in Python 3.10+

var = "name"
match var:
    case "Tom":
        print("Welcome Home!")
    case "Friend":
        print("Welcome back!")
    case _:
        print("Welcome")
"""),
    "MultiProcessing":
        ("built_ins", """from multiprocessing import Pool

list_of_things_that_need_to_be_procesed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def long_function(x):
    result = x * x
    return result


if __name__ == '__main__':
    with Pool(5) as p:
        results = p.map(long_function, list_of_things_that_need_to_be_procesed)

    print(results)
""")
}

layout = html.Div(
    style={
        'margin': 0,
        'padding': 20,
    },
    children=[
        html.Br(),
        html.Br(),
        html.P("While there are many great resources online for learning Python. Many times, I find myself just needing a quick code snippet. So I made this page as a repository of Pythonic things that I use often enough to want a quick and easy way to just get the snippet"),
        html.H3("Python Built in Library"),
        html.Div([
            html.Button(x, id=x, n_clicks=0) for x, v in tips.items() if v[0] == 'built_ins'
        ]),
        html.H3("Python How to"),
        html.Div([
            html.Button(x, id=x, n_clicks=0) for x, v in tips.items() if v[0] == "how_to"
        ]),
        html.Br(),
        # html.Div(id='tip', style={'width': '100%', 'height': 500, 'whiteSpace': 'pre-line'}),
        dcc.Textarea(id='tip', value="", style={'width': '100%', 'height': 300}, spellCheck=False),
    ])


@callback(
    [
        Output('tip', 'value'),
    ],
    [
        Input(x, 'n_clicks') for x in tips.keys()
    ]
)
def displayClick(*args):
    return tips.get(ctx.triggered_id, ("", ""))[1],
