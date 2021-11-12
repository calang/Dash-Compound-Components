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
color_mix2 = ColorMix('color_mix2')
color_mix3 = ColorMix('color_mix3')


app.layout = dbc.Container([
    html.Table([
        html.Tr([
            html.Td(
                [
                    html.Div(id="color-gradient",
                             style=dict(width='200px', height='100px', margin='auto auto 10px auto', padding='20px'),
                             ),
                ],
                colSpan=3
            )
        ]),
        html.Tr([
            html.Td([color_mix1], style=dict(border="1px solid black")),
            html.Td([color_mix2], style=dict(border="1px solid black")),
            html.Td([color_mix3], style=dict(border="1px solid black")),
        ])
    ],  style=dict(border="1px solid black")
    ),
])


@callback(
    Output("color-gradient", 'style'),
    Input(ColorMix.ids.color_mix('color_mix1'), 'style'),
    Input(ColorMix.ids.color_mix('color_mix2'), 'style'),
    Input(ColorMix.ids.color_mix('color_mix3'), 'style'),
    State("color-gradient", 'style'),
)
def update_color_mix(style1, style2, style3, existing_style):

    color1 = style1.get("backgroundColor")
    color2 = style2.get("backgroundColor")
    color3 = style3.get("backgroundColor")

    style_color = existing_style.copy()
    style_color.update(dict(backgroundImage=f"linear-gradient(to right, {color1}, {color2}, {color3})"))

    return style_color


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