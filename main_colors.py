# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import pprint as pp
import dash_bootstrap_components as dbc

from color_components import ColorSlider, ColorMix

from dash import (
    Dash,
    Output, Input, State,
    html, dcc,
    callback, MATCH
)

app = Dash(__name__)

# ---- Try #1:

# c_slider_r = ColorSlider('red', 'color_r')
# c_slider_g = ColorSlider('green', 'color_g')
# c_slider_b = ColorSlider('blue', 'color_b')
#
# app.layout = dbc.Container([
#     html.Div([
#         html.Table([
#             html.Tr([
#                 html.Td([c_slider_r]),
#                 html.Td([c_slider_g]),
#                 html.Td([c_slider_b]),
#             ])
#         ]),
#
#         # layout didn't work: (?)
#
#         # dbc.Row([
#         #     dbc.Col([
#         #         c_slider_r,
#         #     ], width=4),
#         #     dbc.Col([
#         #         c_slider_g,
#         #     ], width=4),
#         #     dbc.Col([
#         #         c_slider_b,
#         #     ], width=4),
#         # ]),
#     ])
# ])

# --- end or Try #1

# --- Try #2


color_mix1 = ColorMix('color_mix1')


app.layout = dbc.Container([
    color_mix1,
    # html.Div([
    #     html.Table([
    #         html.Tr([
    #             html.Td([c_slider_r]),
    #             html.Td([c_slider_g]),
    #             html.Td([c_slider_b]),
    #         ])
    #     ]),
    # ])
])

# --- end of Try #2



PORT = os.getenv("PORTS", 5000)
HOST = os.getenv("HOST", "localhost")

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