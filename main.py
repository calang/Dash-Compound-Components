# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import pprint as pp

from aio_components import MarkdownWithColorAIO
from dash import (
    Dash,
    Output, Input, State,
    html, dcc,
    callback, MATCH
)

app = Dash(__name__)

# Example 1A:
# app.layout = MarkdownWithColorAIO('## Hello World')

# Example 1B:
# app.layout = MarkdownWithColorAIO(
#     'Custom colors',
#     colors=['cornflowerblue', 'darkolivegreen', 'darkslateblue'],
#     dropdown_props={
#         'persistence': True
#     }
# )

#example 1C:
# app.layout = html.Div([
#     html.Div(id='color-picker-output'),
#     MarkdownWithColorAIO(
#         'Custom callback',
#         aio_id='color-picker'
#     ),
# ])

#example 1D:

aio = MarkdownWithColorAIO(
        'Custom callback',
        aio_id='color-picker'
    )

app.layout = html.Div([
    html.Div(id='color-picker-output'),
    aio,
])

pp.pprint(aio.ids.__dict__)
pp.pprint(aio.ids.dropdown('123'))
pp.pprint(aio.children)
pp.pprint(aio.children[0].id)

@app.callback(
    Output('color-picker-output', 'children'),
    Input(MarkdownWithColorAIO.ids.dropdown('color-picker'), 'value')
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
        debug=False,  # APP_DEBUG,
        # ssl_context='adhoc',
        ssl_context=('cert/example.crt', 'cert/example.key'),
    )