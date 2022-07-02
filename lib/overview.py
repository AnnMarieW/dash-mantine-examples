"""
This is the home page which displays an overview of the card grid which shows a preview of the components and examples
"""

import dash
from dash import html, callback, Output, Input, ALL, ctx
import dash_mantine_components as dmc
from lib.utils import search_code_files
from lib.card_grid import make_card_grid


match_case_switch = html.Div(
    [
        dmc.Text("Match Case", size="xs", color="gray"),
        dmc.Switch(
            id="overview-x-case-sensitive",
            checked=False,
            offLabel="OFF",
            onLabel="ON",
            size="lg",
            style={"padding-top": 5},
            persistence=True,
        ),
    ]
)


text_input = dmc.TextInput(label="Code Search", id="overview-x-code-search-input")

search_code_div = dmc.Group([text_input, match_case_switch], spacing="xs")


def filtered_registry(filtered_example_app_list):
    """
    Returns a filtered dash.page_registry dict based on a list of example app names
    """

    # We use the module param to filter the dash_page_registry
    # Note that the module name includes the pages folder name eg: "pages.bar-charts"
    filtered_registry = []
    for page in dash.page_registry.values():
        filename = page["module"].split("pages.")[1]
        if filename in filtered_example_app_list:
            filtered_registry.append(page)
    return filtered_registry


def layout(filter=None, *other):
    """
    Displays the apps in a card grid.
    May pass query stings to filter the examples.
    If using query strings, the variable name must be `filter`.  eg `http://127.0.0.1:8050/?filter=dropdown`
    """
    print("filter", filter)

    if filter:
        # filter apps based on query strings
        filtered_example_app_names = search_code_files(filter, case_sensitive=True)
        registry = filtered_registry(filtered_example_app_names)
        children = make_card_grid(registry=registry)
    else:
        # show all apps
        children = make_card_grid(registry=dash.page_registry.values())

    return html.Div(
        [search_code_div, html.Div(id="overview-x-grid", children=children)],
        style={"padding": 20},
    )


@callback(
    Output("overview-x-grid", "children"),
    Output("overview-x-code-search-input", "value"),
    Input("overview-x-code-search-input", "value"),
    Input("overview-x-case-sensitive", "checked"),
    prevent_initial_call=True,
)
def update(searchterms, case_sensitive):
    print("CS", case_sensitive)
    input_id = ctx.triggered_id
    registry = dash.page_registry.values()

    # show apps based on search field
    if input_id == "overview-x-code-search-input":
        if searchterms:
            filtered_example_app_names = search_code_files(searchterms, case_sensitive)
            registry = filtered_registry(filtered_example_app_names)
            return make_card_grid(registry=registry), dash.no_update
    return make_card_grid(registry=registry), None
