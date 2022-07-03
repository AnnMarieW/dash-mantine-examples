import dash
from dash import Dash, html, dcc, Input, Output, State, ctx, clientside_callback
import dash_mantine_components as dmc


from lib.utils import example_apps, example_source_codes, file_name_from_path

scripts = [
    "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/dayjs.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/locale/ru.min.js",
]

app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    use_pages=True,
    external_scripts=scripts,
)

for k in example_apps:
    new_callback_map = example_apps[k].callback_map
    new_callback_list = example_apps[k]._callback_list

    app.callback_map.update(new_callback_map)
    app._callback_list.extend(new_callback_list)


fullscreen_modal = dmc.Modal(
    children=html.Div(id="content-fs"), title="Size: full", id="modal-fs", size="full"
)


def create_home_link(label):
    return dmc.Text(
        label,
        size="xl",
        color="gray",
    )


def create_header():
    return dmc.Header(
        height=70,
        fixed=True,
        p="md",
        children=[
            dmc.Container(
                fluid=True,
                style={"paddingRight": 12, "paddingLeft": 12},
                children=dmc.Group(
                    position="apart",
                    align="flex-start",
                    children=[
                        dmc.Center(
                            dcc.Link(
                                [
                                    dmc.MediaQuery(
                                        create_home_link(
                                            "Dash Mantine Components Examples"
                                        ),
                                        smallerThan="sm",
                                        styles={"display": "none"},
                                    ),
                                    dmc.MediaQuery(
                                        create_home_link("DMC Examples"),
                                        largerThan="sm",
                                        styles={"display": "none"},
                                    ),
                                ],
                                href="/",
                                style={"paddingTop": 3, "textDecoration": "none"},
                            ),
                        ),
                        dmc.Group(
                            position="right",
                            align="center",
                            # spacing="xl",
                            children=[
                                dmc.Button(
                                    "Fullscreen App",
                                    id="open-fs-app",
                                    color="gray",
                                    variant="light",
                                    style={"display": "none"},
                                ),
                                dmc.Button(
                                    "Fullscreen Code",
                                    id="open-fs-code",
                                    color="gray",
                                    variant="light",
                                    style={"display": "none"},
                                ),
                                html.A(
                                    dmc.Button(
                                        "dmc-docs",
                                        id="dmc-docs",
                                        color="gray",
                                        variant="light",
                                    ),
                                    href="https://www.dash-mantine-components.com/",
                                    target="_blank",
                                ),
                                html.A(
                                    dmc.Button(
                                        "Overview",
                                        id="overview",
                                        color="gray",
                                        variant="light",
                                    ),
                                    href="/",
                                ),
                                dmc.ThemeSwitcher(
                                    id="color-scheme-toggle",
                                    style={"cursor": "pointer"},
                                ),
                            ],
                        ),
                    ],
                ),
            )
        ],
    )


app.layout = dmc.MantineProvider(
    id="theme-provider",
    theme={
        "colorScheme": "light",
        "fontFamily": "'Inter', sans-serif",
        "primaryColor": "indigo",
    },
    styles={
        "Button": {"root": {"fontWeight": 400}},
        "Alert": {"title": {"fontWeight": 500}},
        "AvatarsGroup": {"truncated": {"fontWeight": 500}},
    },
    withGlobalStyles=True,
    withNormalizeCSS=True,
    children=[
        create_header(),
        dmc.Space(h=40),
        fullscreen_modal,
        dmc.Container(dash.page_container, fluid=True, style={"marginTop": "4rem"}),
        dcc.Location(id="url", refresh=True),
    ],
)


@app.callback(
    Output("open-fs-app", "style"),
    Output("open-fs-code", "style"),
    Input("url", "pathname"),
)
def fullscreen(path):
    """Don't show full screen buttons on home page (overview)"""
    if path == "/":
        return {"display": "none"}, {"display": "none"}
    return {}, {}


@app.callback(
    Output("modal-fs", "opened"),
    Output("content-fs", "children"),
    Input("open-fs-app", "n_clicks"),
    Input("open-fs-code", "n_clicks"),
    State("modal-fs", "opened"),
    State("url", "pathname"),
)
def toggle_modal(n_app, n_code, is_open, pathname):
    filename = file_name_from_path(pathname)
    layout = None
    code = None
    if filename in example_apps:
        layout = example_apps[filename].layout
        code = example_source_codes[filename].replace(filename + "-x-", "")
        code = dmc.Prism(
            language="python",
            children=code,
            colorScheme="dark",
            # noCopy=True
        )
    content = layout if ctx.triggered_id == "open-fs-app" else code

    if n_app or n_code:
        return not is_open, content
    return is_open, content


@app.callback(
    Output("url", "href"), Input("modal-fs", "opened"), State("url", "pathname")
)
def refresh_page(is_open, pathname):
    """refreshes screen when full screen mode is closed, else example app callbacks don't fire"""
    if is_open is None:
        return dash.no_update
    return pathname if not is_open else dash.no_update


clientside_callback(
    """function(colorScheme) {
        return {
            colorScheme,
            fontFamily: "'Inter', sans-serif",
            primaryColor: "indigo"
        }
    }""",
    Output("theme-provider", "theme"),
    Input("color-scheme-toggle", "value"),
)


if __name__ == "__main__":
    app.run_server(debug=True)
