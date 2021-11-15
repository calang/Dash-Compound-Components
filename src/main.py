"""Demonstration of nested Dash compound components."""

import os
import dash_bootstrap_components as dbc

from dash import (
    Dash,
    Output, Input, State,
    html,
    callback
)

from color_components import ColorMix


app = Dash(__name__,
           external_stylesheets=[dbc.themes.BOOTSTRAP]
           )

color_mix1 = ColorMix('color_mix1')
color_mix2 = ColorMix('color_mix2')
color_mix3 = ColorMix('color_mix3')

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([html.Div(id="color-gradient",
                          style=dict(width='200px', height='100px',
                                     margin='10px auto 10px auto',
                                     padding='20px',
                                     border='1px solid black',
                                     ),
                          ),
                 ]),
    ]),
    dbc.Row([
        dbc.Col([color_mix1], width=4),
        dbc.Col([color_mix2], width=4),
        dbc.Col([color_mix3], width=4),
    ]),
], fluid=True
)


@callback(
    Output("color-gradient", 'style'),
    Input(ColorMix.ids.color_mix('color_mix1'), 'style'),
    Input(ColorMix.ids.color_mix('color_mix2'), 'style'),
    Input(ColorMix.ids.color_mix('color_mix3'), 'style'),
    State("color-gradient", 'style'),
)
def update_color_mix(style1, style2, style3, existing_style):
    """
    Change the background color in existing_style
    to a 3-way gradient formed with thebackgroundColor-s in the input styles.
    """

    color1 = style1.get("backgroundColor")
    color2 = style2.get("backgroundColor")
    color3 = style3.get("backgroundColor")

    style_color = existing_style.copy()
    style_color.update(
        dict(backgroundImage=f"linear-gradient(to right, {color1}, {color2}, {color3})")
    )

    return style_color


PORT = os.getenv("PORTS", '5000')
HOST = os.getenv("HOST", "localhost")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run_server(
        host=HOST,
        port=PORT,
        debug=False,
        # ssl_context='adhoc',
        ssl_context=('cert/example.crt', 'cert/example.key'),
    )
