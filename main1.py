# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import pprint as pp

from aio_components1 import MarkdownWithColorAIO
from dash import (
    Dash,
    Output, Input, State,
    html, dcc,
    callback, MATCH
)

app = Dash(__name__)


aio1 = MarkdownWithColorAIO(
        'Custom callback',
        aio_id='color-picker1'
    )
aio2 = MarkdownWithColorAIO(
        'Custom callback',
        aio_id='color-picker2'
    )

app.layout = html.Div([
    html.Div(id='color-picker-output1'),
    aio1,
    html.Div(id='color-picker-output2'),
    aio2,
])

# pp.pprint(aio1.ids.__dict__)
# pp.pprint(aio1.ids.dropdown('123'))
# pp.pprint(aio1.children)
pp.pprint(aio1.children[0].id)
pp.pprint(MarkdownWithColorAIO.ids.dropdown('color-picker1'))
pp.pprint(MarkdownWithColorAIO.dropdown_id('color-picker1'))


@app.callback(
    Output('color-picker-output1', 'children'),
    Input(MarkdownWithColorAIO.ids.dropdown('color-picker1'), 'value')
)
def display_color(value):
    return f'You have selected {value}'

@app.callback(
    Output('color-picker-output2', 'children'),
    Input(MarkdownWithColorAIO.ids.dropdown('color-picker2'), 'value')
)
def display_color(value):
    return f'You have selected {value}'



PORT = os.getenv("PORTS", 5000)
HOST = os.getenv("HOST", "0.0.0.0")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # NOTE: If debug is set to True, it will automatically set logging level to INFO.
    # To get DEBUG printouts, APP_DEBUG must be set to False and LOG_LEVEL to DEBUG.
    app.run_server(
        host=HOST,
        port=PORT,
        debug=True,  # APP_DEBUG,
        # ssl_context='adhoc',
        ssl_context=('cert/example.crt', 'cert/example.key'),
    )