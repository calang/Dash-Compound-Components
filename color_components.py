import uuid

from dash import Dash, Output, Input, State, html, dcc, callback, MATCH
import dash_daq as daq

from color_util import color_intensity_to_hex, rgb_hex_color_add


class ColorSlider(html.Div):
    class Ids:
        @staticmethod
        def color_block(color_slider_id: str):
            return color_slider_id + '-color_block'

        @staticmethod
        def knob(color_slider_id: str):
            return color_slider_id + '-knob'

    # Make the ids class a public class
    ids = Ids

    # @classmethod
    # def color_block_id(cls, color_slider_id):
    #     return color_slider_id + '-color_block-ColorSlider'
    #
    # @classmethod
    # def knob_id(cls, color_slider_id):
    #     return color_slider_id + '-knob-ColorSlider'

    # Define the initializers of the ColorSlider component
    def __init__(
        self,
        color: str = 'red',  # one of 'red', 'green', 'blue'
        color_slider_id=None,
    ):
        """
        ColorSlider: a composite component inheriting from `html.Div`

        Composed of:
            - `color_block`: `html.Div` with the adjusted color as its backgroundColor style property
            - `knob`: `dcc.knob`

        Initialization properties:
            - `color` - color for the knob
            - `color_slider_id` - ColorSlider id; optional, with randomly generated value as default

        SubComponent IDs:
            - ColorSlider.ids.knob(`color_slider_id`)
            - ColorSlider.ids.color_block(`color_slider_id`)
        """

        # Allow developers to pass in their own `color_slider_id`
        # if they're binding their own callbacks to a particular component.
        if color_slider_id is None:
            color_slider_id = str(uuid.uuid4())

        # validate color and adjust to default if needed
        if color not in {'red', 'green', 'blue'}:
            color = 'red'

        # Define the component's layout
        super().__init__(
            [  # Equivalent to `html.Div([...])`
                html.Div(id=self.ids.color_block(color_slider_id),
                         style=dict(width='50px', height='100px', margin='auto auto 10px auto', padding='20px'),
                         # , border='1px solid black')),
                         ),
                # html.Br(),
                daq.Knob(id=self.ids.knob(color_slider_id),
                         label="Level of " + color,
                         size=100,
                         max=255,
                         value=200,
                         # scale={'start': 0, 'labelInterval': 64, 'interval': 32}
                         ),
            ],
        )

        # Define the callbacks, specific for this ColorSlider instance

        @callback(
            Output(self.ids.knob(color_slider_id), 'label'),
            Input(self.ids.knob(color_slider_id), 'value'),
        )
        def update_output(value):
            """Update the label of the knob with the knob color and level"""
            return f"Level of {color}: {int(value)}"

        @callback(
            Output(self.ids.color_block(color_slider_id), 'style'),
            Input(self.ids.knob(color_slider_id), 'value'),
            State(self.ids.color_block(color_slider_id), 'style'),
        )
        def update_color_block_style(intensity, existing_style):
            """Update the backgroundColor style of the color_block with the intensity level from the knob"""
            existing_style['backgroundColor'] = color_intensity_to_hex(color, intensity)
            return existing_style


class ColorMix(html.Div):
    class Ids:
        @staticmethod
        def color_mix(color_mixer_id: str):
            return color_mixer_id + '-color_mix'

        @staticmethod
        def r_slider(color_mixer_id: str):
            return color_mixer_id + '-r_slider'

        @staticmethod
        def g_slider(color_mixer_id: str):
            return color_mixer_id + '-g_slider'

        @staticmethod
        def b_slider(color_mixer_id: str):
            return color_mixer_id + '-b_slider'

    # Make the ids class a public class
    ids = Ids

    # Define the initializers of the ColorMixer component
    def __init__(self, color_mixer_id=None):
        """
        ColorMix: a composite component mixing the colors from its three internal `ColorSlider`s

        Composed of
            - `color_mixer`: html.Div showing the result of mixing the colors in the ColorSlider-s
            - `r_slider`: ColorSlider to define the level of red to use
            - `g_slider`: ColorSlider to define the level of green to use
            - `b_slider`: ColorSlider to define the level of blue to use

        Initialization properties:
            - `color_mixer_id`: in case the developer wants to assign a specific id,
                to write callbacks on the subcomponents.

        SubComponent IDs:
            - ColorMixer.ids.color_mixer(`color_mixer_id`)
            - ColorMixer.ids.r_slider(`color_mixer_id`)
            - ColorMixer.ids.g_slider(`color_mixer_id`)
            - ColorMixer.ids.b_slider(`color_mixer_id`)
        """

        # Allow developers to pass in their own `color_mixer_id`
        # if they're binding their own callbacks to a particular component.
        if color_mixer_id is None:
            color_mixer_id = str(uuid.uuid4())

        # created here for readability; might as well have been created within the html.Div, below.
        r_slider = ColorSlider('red', self.ids.r_slider(color_mixer_id))
        g_slider = ColorSlider('green', self.ids.g_slider(color_mixer_id))
        b_slider = ColorSlider('blue', self.ids.b_slider(color_mixer_id))

        # Define the component's layout
        super().__init__(
            [  # Equivalent to `html.Div([...])`
                html.Table([
                    html.Tr([
                        html.Td(
                            [
                                html.Div(id=self.ids.color_mix(color_mixer_id),
                                         style=dict(width='50px', height='100px', margin='auto auto 10px auto',
                                                    padding='20px'),
                                         ),
                            ],
                            colSpan=3
                        )
                    ]),
                    html.Tr([
                        html.Td([r_slider]),
                        html.Td([g_slider]),
                        html.Td([b_slider]),
                    ])
                ]),
            ],
        )

        # Define the callbacks, specific for this ColorMix instance

        @callback(
            Output(self.ids.color_mix(color_mixer_id), 'style'),
            Input(ColorSlider.ids.color_block(self.ids.r_slider(color_mixer_id)), 'style'),
            Input(ColorSlider.ids.color_block(self.ids.g_slider(color_mixer_id)), 'style'),
            Input(ColorSlider.ids.color_block(self.ids.b_slider(color_mixer_id)), 'style'),
            State(self.ids.color_mix(color_mixer_id), 'style'),
        )
        def update_color_mix(r_color, g_color, b_color, existing_style):
            style_color = rgb_hex_color_add(r_color.get('backgroundColor'),
                                            g_color.get('backgroundColor'),
                                            b_color.get('backgroundColor'),
                                            )
            existing_style['backgroundColor'] = style_color
            return existing_style
