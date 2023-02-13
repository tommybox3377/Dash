import base64
import os
from uuid import uuid4

import dash
from dash import html, dcc, callback, Input, Output, State
import whisper
from wordcloud import WordCloud

stop_words = set("""a
about
above
after
again
against
all
am
an
and
any
are
aren't
as
at
be
because
been
before
being
below
between
both
but
by
can't
cannot
could
couldn't
did
didn't
do
does
doesn't
doing
don't
down
during
each
few
for
from
further
had
hadn't
has
hasn't
have
haven't
having
he
he'd
he'll
he's
her
here
here's
hers
herself
him
himself
his
how
how's
i
i'd
i'll
i'm
i've
if
in
into
is
isn't
it
it's
its
itself
let's
me
more
most
mustn't
my
myself
no
nor
not
of
off
on
once
only
or
other
ought
our
ours
ourselves
out
over
own
same
shan't
she
she'd
she'll
she's
should
shouldn't
so
some
such
than
that
that's
the
their
theirs
them
themselves
then
there
there's
these
they
they'd
they'll
they're
they've
this
those
through
to
too
under
until
up
very
was
wasn't
we
we'd
we'll
we're
we've
were
weren't
what
what's
when
when's
where
where's
which
while
who
who's
whom
why
why's
with
won't
would
wouldn't
you
you'd
you'll
you're
you've
your
yours
yourself
yourselves""".split("\n"))

dash.register_page(__name__)

layout = html.Div(
    style={
        "margin-left": "18rem",
        "margin-right": "2rem",
        "padding": "2rem 1rem",
    },
    children=[
        dcc.Upload(
            id='audio',
            children=html.Div([
                html.A('Drag and Drop or Select Files')
            ]),
            style={
                'width': '100%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px'
            },

            multiple=False
        ),
        html.Br(),
        dcc.Loading(
            id="loading-1",
            children=[html.Div([html.Img(id="cloud", src="")], style={'textAlign': 'center'})],
            type="default"
        ),
        html.Br(),
        html.Br(),
        dcc.Loading(
            id="loading-2",
            children=[html.P("", id='words', style={'width': '100%', 'display': 'inline-block', 'text-align': 'center'})],
            type="default"
        ),
    ])


def audio_to_text(fname):
    print("I am here!")
    model = whisper.load_model("tiny.en")
    results = model.transcribe(fname)["text"]
    os.remove(fname)
    return results

def make_wordcloud(all_words, fname):
    wc = WordCloud(background_color="rgba(255, 255, 255, 0)",
                    mode="RGBA",
                    collocations=False,
                    width=500,
                    height=300,
                    contour_width=3,
                    contour_color='black',
                    stopwords=stop_words)
    wc.generate(all_words)
    wc.to_file(f'assets/cloudfiles/{fname}.png')


@callback(
    Output('words', 'children'),
    Output('cloud', 'src'),
    Input('audio', 'contents'),
    State('audio', 'filename'),
)
def update_output(audio_file, incoming_name):
    if audio_file:
        if incoming_name.split(".")[-1] not in ["mp3", "m4a"]:
            return ".mp3 files only, Sorry!", f'assets/typeerror.png'
        try:
            print(incoming_name)
            content_type, content_string = audio_file.split(',')

            if len(content_string) > 20_000_000:
                return "Audio is too long, please contact me to use longer audio clips!", f'assets/lenerror.png'
            print(len(content_string))

            decoded = base64.b64decode(content_string)

            fname = str(uuid4())

            with open(f"WIP/{fname}.mp3", "wb") as file:
                file.write(decoded)

            print("Trigger!")
            text = audio_to_text(f"WIP/{fname}.mp3")
            print("clouding!")
            make_wordcloud(text, fname)
            return text, f'assets/cloudfiles/{fname}.png'
        except Exception as ex:
            print(ex)
            return "Something went wrong, sorry!", f'assets/error.png'
    else:
        return "Here will be my into! I like talking!", "assets/wordcloud.png"
