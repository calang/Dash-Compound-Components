from dash import Dash, Output, Input, State, html, dcc, callback, MATCH
import uuid

# All-in-One Components should be suffixed with 'AIO'
class MarkdownWithColorAIO(html.Div):  # html.Div will be the "parent" component
    # A set of functions that create pattern-matching callbacks of the sub-components
    class ids:
        dropdown = lambda aio_id: {
            'comp': 'MarkdownWithColorAIO-dropdown',
            'aio_id': aio_id
        }
        markdown = lambda aio_id: {
            'comp': 'MarkdownWithColorAIO-markdown',
            # this causes a TypeError: dict id values must be strings, numbers or bools
            # 'extra': {'embedded': 1},
            'aio_id': aio_id
        }

    # Make the ids class a public class
    ids = ids

    # Define the arguments of the All-in-One component
    def __init__(
        self,
        text,
        colors=['#001f3f', '#0074D9', '#85144b', '#3D9970'],
        markdown_props={},
        dropdown_props={},
        aio_id=None
    ):
        """
        MarkdownWithColorAIO is an All-in-One component inheriting from `html.Div`

        It is composed of
            * a `dcc.Dropdown` color picker ("`dropdown`")
            * a `dcc.Markdown` ("`markdown`") component
        as children.

        The markdown component's color is determined by the dropdown colorpicker.
        - `text` - The Markdown component's text (required)
        - `colors` - The colors displayed in the dropdown
        - `markdown_props` - A dictionary of properties passed into the dcc.Markdown component. See https://dash.plotly.com/dash-core-components/markdown for the full list.
        - `dropdown_props` - A dictionary of properties passed into the dcc.Dropdown component. See https://dash.plotly.com/dash-core-components/dropdown for the full list.
        - `aio_id` - The All-in-One component ID used to generate the markdown and dropdown components's dictionary IDs.

        The All-in-One component dictionary IDs are available as
        - MarkdownWithColorAIO.ids.dropdown(aio_id)
        - MarkdownWithColorAIO.ids.markdown(aio_id)
        """

        # Allow developers to pass in their own `aio_id` if they're
        # binding their own callback to a particular component.
        if aio_id is None:
            # Otherwise use a uuid that has virtually no chance of collision.
            # Uuids are safe in dash deployments with processes
            # because this component's callbacks
            # use a stateless Pattern-Matching Callback:
            # The actual ID does not matter as long as its unique and matches
            # the PMC `MATCH` pattern..
            aio_id = str(uuid.uuid4())

        # Merge user-supplied properties into default properties
        dropdown_props = dropdown_props.copy()  # copy the dict so as to not mutate the user's dict
        if 'options' not in dropdown_props:
            dropdown_props['options'] = [{'label': i, 'value': i} for i in colors]
        dropdown_props['value'] = dropdown_props['options'][0]['value']

        # Merge user-supplied properties into default properties
        markdown_props = markdown_props.copy()  # copy the dict so as to not mutate the user's dict
        if 'style' not in markdown_props:
            markdown_props['style'] = {'color': dropdown_props['value']}
        if 'children' not in markdown_props:
            markdown_props['children'] = text

        # Define the component's layout
        super().__init__([  # Equivalent to `html.Div([...])`
            dcc.Markdown(id=self.ids.markdown(aio_id), **markdown_props),
            dcc.Dropdown(id=self.ids.dropdown(aio_id), **dropdown_props),
        ])

    # Define this component's stateless Pattern-Matching Callback
    # that will apply to every instance of this component.
    @callback(
        Output(ids.markdown(MATCH), 'style'),
        Input(ids.dropdown(MATCH), 'value'),
        State(ids.markdown(MATCH), 'style'),
    )
    def update_markdown_style(color, existing_style):
        existing_style['color'] = color
        return existing_style