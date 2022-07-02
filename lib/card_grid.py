import dash
from dash import html, dcc
import dash_mantine_components as dmc


def make_header(label):
    return dmc.Text(
        label,
        size="xl",
        color="gray",
    )


def make_docs_btn(path):
    if path:
        component_name = path.split("/")[-1]
        button_label = f"dmc-docs {component_name}"
        return html.A(
            dmc.Button(
                button_label,
                id="docs",
                color="gray",
                variant="light",
            ),
            href=f"https://www.dash-mantine-components.com{path}",
            target="_blank",
        )


def make_card(page):
    from dash_labs import print_registry

    print_registry(exclude="layout")

    return dmc.Paper(
        [
            html.Div(
                [
                    html.A(
                        html.Div(
                            [
                                make_header(page.get("card_title", page["name"])),
                                dmc.Divider(style={"margin-bottom": 20}),
                                dmc.Image(
                                    src=dash.get_asset_url(page["image"]),
                                    # height=300,
                                    fit="contain",
                                ),
                            ]
                        ),
                        href=page["path"],
                        style={"paddingTop": 3, "textDecoration": "none"},
                    ),
                    dmc.Divider(style={"margin": "10px 0px"}),
                    make_docs_btn(page.get("dmc_docs_path")),
                ]
            ),
        ],
        shadow="lg",
        p=40,
    )


def make_card_grid(registry=None):
    if registry is None:
        registry = dash.page_registry.values()

    return dmc.Grid(
        [
            dmc.Col(html.Div(make_card(page)), sm=6, lg=4)
            for page in registry
            if page["path"] != "/"
        ],
        gutter="sm",
    )
