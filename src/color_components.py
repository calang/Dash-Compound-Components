"""Dash Compound Components demo, handling color mixtures"""
# pylint: disable=too-few-public-methods,import-error

import uuid

from dash import Output, Input, State, html, callback
import dash_bootstrap_components as dbc
import dash_daq as daq

from color_util import color_value_to_hex, rgb_hex_color_add


class ColorMix(html.Div):
    """Show three basic color levels and the resulting mixed color."""

    class Ids:
        """Return ids of internal components."""

        @staticmethod
        def color_mix(color_mixer_id: str):
            """Return id for the color mix display box"""
            return color_mixer_id + '-color_mix'

        @staticmethod
        def r_knob(color_mixer_id: str):
            """Return id for the red level knob"""
            return color_mixer_id + '-r_knob'

        @staticmethod
        def g_knob(color_mixer_id: str):
            """Return id for the green level knob"""
            return color_mixer_id + '-g_knob'

        @staticmethod
        def b_knob(color_mixer_id: str):
            """Return id for the blue level knob"""
            return color_mixer_id + '-b_knob'

    # Make the ids class a public class
    ids = Ids

    # Define the initializers of the ColorMixer component
    def __init__(self, color_mixer_id=None):
        """
        ColorMix: a compound component mixing the colors from three internal `ColorLevelCC`s

        Composed of
            - `color_mixer`: html.Div showing the result of mixing the colors in the ColorLevelCC-s
            - `r_knob`: ColorLevelCC to define the level of red to use
            - `g_knob`: ColorLevelCC to define the level of green to use
            - `b_knob`: ColorLevelCC to define the level of blue to use

        Initialization properties:
            - `color_mixer_id`: in case the developer wants to assign a specific id,
                to write callbacks on the subcomponents.

        SubComponent IDs:
            - ColorMixer.ids.color_mixer(`color_mixer_id`)
            - ColorMixer.ids.r_knob(`color_mixer_id`)
            - ColorMixer.ids.g_knob(`color_mixer_id`)
            - ColorMixer.ids.b_knob(`color_mixer_id`)
        """

        # Allow developers to pass in their own `color_mixer_id`
        # if they're binding their own callbacks to a particular component.
        if color_mixer_id is None:
            color_mixer_id = str(uuid.uuid4())

        # created here for readability; might as well have been created within the html.Div, below.
        r_knob = ColorLevelCC('red', self.ids.r_knob(color_mixer_id))
        g_knob = ColorLevelCC('green', self.ids.g_knob(color_mixer_id))
        b_knob = ColorLevelCC('blue', self.ids.b_knob(color_mixer_id))

        # Define the component's layout
        super().__init__(
            [
                dbc.Row([
                    dbc.Col([
                        html.Div(id=self.ids.color_mix(color_mixer_id),
                                 style=dict(width='50px', height='100px',
                                            margin='auto auto 10px auto',
                                            padding='20px',
                                            border='1px solid black',
                                            ),
                                 ),
                    ]),
                ]),
                dbc.Row([
                    dbc.Col([r_knob], width=4),
                    dbc.Col([g_knob], width=4),
                    dbc.Col([b_knob], width=4),
                ]),
            ],
            style=dict(border='1px solid black', padding='10px')
        )

        # Callbacks, specific for this ColorMix instance

        @callback(
            Output(self.ids.color_mix(color_mixer_id), 'style'),
            Input(ColorLevelCC.ids.color_block(self.ids.r_knob(color_mixer_id)), 'style'),
            Input(ColorLevelCC.ids.color_block(self.ids.g_knob(color_mixer_id)), 'style'),
            Input(ColorLevelCC.ids.color_block(self.ids.b_knob(color_mixer_id)), 'style'),
            State(self.ids.color_mix(color_mixer_id), 'style'),
        )
        def update_color_mix(r_color, g_color, b_color, existing_style):
            """
            Add the primary colors from the ColorLevelCC-s
            showing the result as the backgroundColor of the color_mix block.
            """
            style_color = rgb_hex_color_add(r_color.get('backgroundColor'),
                                            g_color.get('backgroundColor'),
                                            b_color.get('backgroundColor'),
                                            )
            existing_style['backgroundColor'] = style_color
            return existing_style


class ColorLevelCC(html.Div):
    """Class a the 3-way color gradient formed with three editable colors."""

    class Ids:
        """Return ids of internal components."""

        @staticmethod
        def color_block(color_level_id: str):
            """Return id for the color value display box"""
            return color_level_id + '-color_block'

        @staticmethod
        def knob(color_level_id: str):
            """Return id for the color value knob"""
            return color_level_id + '-knob'

    # Make the ids class a public class
    ids = Ids

    # Define the initializers of the ColorLevelCC
    def __init__(
        self,
        color: str = 'red',  # one of 'red', 'green', 'blue'
        color_level_id=None,
    ):
        """
        ColorLevelCC: a composite component inheriting from `html.Div`

        Composed of:
            - `color_block`: `html.Div` with the adjusted backgroundColor style property
            - `knob`: `dcc.knob`

        Initialization properties:
            - `color` - color for the knob
            - `color_level_id` - ColorLevelCC id; optional, with randomly generated value as default

        SubComponent IDs:
            - ColorLevelCC.ids.knob(`color_level_id`)
            - ColorLevelCC.ids.color_block(`color_level_id`)
        """

        # Allow developers to pass in their own `color_level_id`
        # if they're binding their own callbacks to a particular component.
        if color_level_id is None:
            color_level_id = str(uuid.uuid4())

        # validate color and adjust to default if needed
        if color not in {'red', 'green', 'blue'}:
            color = 'red'

        # Define the component's layout
        super().__init__(
            [  # Equivalent to `html.Div([...])`
                html.Div(id=self.ids.color_block(color_level_id),
                         style=dict(width='50px', height='100px',
                                    margin='10px auto 10px auto',
                                    border='1px solid black',
                                    ),
                         ),
                daq.Knob(id=self.ids.knob(color_level_id),
                         label="Level of " + color,
                         size=100,
                         min=0,
                         max=255,
                         value=200,
                         scale={'labelInterval': 1, 'interval': 128}
                         ),
            ],
            style=dict(border='1px solid black')
        )

        # Callbacks, specific for this ColorLevelCC instance

        @callback(
            Output(self.ids.knob(color_level_id), 'label'),
            Input(self.ids.knob(color_level_id), 'value'),
        )
        def update_output(value):
            """Update the label of the knob with the knob color and level"""
            return f"Level of {color}: {int(value)}"

        @callback(
            Output(self.ids.color_block(color_level_id), 'style'),
            Input(self.ids.knob(color_level_id), 'value'),
            State(self.ids.color_block(color_level_id), 'style'),
        )
        def update_color_block_style(value, existing_style):
            """
            Update the backgroundColor style of the color_block
            with the value level from the knob
            """
            existing_style['backgroundColor'] = color_value_to_hex(color, value)
            return existing_style
