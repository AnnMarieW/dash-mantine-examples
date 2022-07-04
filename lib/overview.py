"""
This is the home page which displays an overview of the card grid which shows a preview of the components and examples
"""

import dash
from dash import html, callback, Output, Input, ALL, ctx
import dash_mantine_components as dmc
from lib.utils import filter_registry
from lib.card_grid import make_card_grid


def make_search_code(code_filter):

    match_case_switch = html.Div(
        [
            dmc.Text("Match Case", size="xs", color="gray"),
            dmc.Switch(
                id="overview-x-case-sensitive",
                checked=False,
                offLabel="OFF",
                onLabel="ON",
                size="lg",
                style={"paddingTop": 5},
                persistence="true",
            ),
        ],
    )
    text_input = dmc.TextInput(
        value=code_filter, label="Code Search", id="overview-x-code-search-input"
    )
    return dmc.Group([text_input, match_case_switch], spacing="xs")


def layout(filter=None, **other):
    """
    Displays the apps in a card grid.
    May pass query stings to filter the examples.
    If using query strings, the variable name must be `filter`.  eg `http://127.0.0.1:8050/?filter=dropdown`
    """

    return html.Div(
        [make_search_code(filter), dmc.Space(h=20), html.Div(id="overview-x-grid")],
        style={"padding": 20},
    )


@callback(
    Output("overview-x-grid", "children"),
    Output("overview-x-code-search-input", "value"),
    Input("overview-x-code-search-input", "value"),
    Input("overview-x-case-sensitive", "checked"),
    Input("color-scheme-toggle", "value"),
)
def update(searchterms, case_sensitive, theme):
    if searchterms:
        # show apps based on search field
        registry = filter_registry(searchterms, case_sensitive)
        return make_card_grid(registry=registry, theme=theme), dash.no_update

    # show all apps
    return make_card_grid(registry=dash.page_registry.values(), theme=theme), None
