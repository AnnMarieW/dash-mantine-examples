import dash_mantine_components as dmc
from dash import Dash, html
from dash_iconify import DashIconify

app = Dash(__name__)

import dash_mantine_components as dmc

colors = [
    "gray",
    "red",
    "pink",
    "grape",
    "violet",
    "indigo",
    "blue",
    "lime",
    "yellow",
    "orange",
]

badge_colors = dmc.Group(
    direction="column",
    spacing="xs",
    position="center",
    children=[
        dmc.Group(
            [dmc.Badge(color, variant=variant, color=color) for color in colors],
            position="center",
        )
        for variant in ["light", "outline", "filled", "dot"]
    ],
)

badge_gradient = dmc.Group(
    children=[
        dmc.Badge(
            "Indigo cyan",
            variant="gradient",
            gradient={"from": "indigo", "to": "cyan"},
        ),
        dmc.Badge(
            "Lime green",
            variant="gradient",
            gradient={"from": "teal", "to": "lime", "deg": 105},
        ),
        dmc.Badge(
            "Teal blue",
            variant="gradient",
            gradient={"from": "teal", "to": "blue", "deg": 60},
        ),
        dmc.Badge(
            "Orange red",
            variant="gradient",
            gradient={"from": "orange", "to": "red"},
        ),
        dmc.Badge(
            "Grape pink",
            variant="gradient",
            gradient={"from": "grape", "to": "pink", "deg": 35},
        ),
    ]
)

badge_size = dmc.Group(
    [
        dmc.Badge("Sale", size="xs"),
        dmc.Badge("Sale", size="sm"),
        dmc.Badge("Sale", size="md"),
        dmc.Badge("Sale", size="lg"),
        dmc.Badge("Sale", size="xl"),
    ]
)

badge_radius = dmc.Group(
    [
        dmc.Badge("Sale", radius="xs"),
        dmc.Badge("Sale", radius="sm"),
        dmc.Badge("Sale", radius="md"),
        dmc.Badge("Sale", radius="lg"),
        dmc.Badge("Sale", radius="xl"),
    ]
)


app.layout = dmc.Container(
    [
        html.Div(
            [
                dmc.Title("Badge colors", order=4, style={"marginBottom": 10}),
                badge_colors,
            ],
        ),
        dmc.Space(h=75),
        html.Div(
            [
                dmc.Title(
                    "Badge with gradient fill", order=4, style={"marginBottom": 10}
                ),
                badge_gradient,
            ],
        ),
        dmc.Space(h=75),
        html.Div(
            [dmc.Title("Badge size", order=4, style={"marginBottom": 10}), badge_size],
        ),
        dmc.Space(h=75),
        html.Div(
            [
                dmc.Title("Badge radius", order=4, style={"marginBottom": 10}),
                badge_radius,
            ],
        ),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
