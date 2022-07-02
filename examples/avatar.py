import dash_mantine_components as dmc
from dash import Dash, html
from dash_iconify import DashIconify

app = Dash(__name__)

avatars = [
    dmc.Avatar(src="https://avatars.githubusercontent.com/u/91216500?v=4", radius="xl"),
    # default placeholder
    dmc.Avatar(radius="xl"),
    # initials
    dmc.Avatar("MK", color="cyan", radius="xl"),
    # icon
    dmc.Avatar(DashIconify(icon="radix-icons:star"), color="blue", radius="xl"),
]

simple_example = dmc.Group(avatars)


avatar_with_tooltip = html.A(
    dmc.Tooltip(
        dmc.Avatar(
            src="https://e7.pngegg.com/pngimages/799/987/png-clipart-computer-icons-avatar-icon-design-avatar-heroes"
            "-computer-wallpaper-thumbnail.png",
            size="lg",
            radius="xl",
        ),
        label="Snehil Vijay",
        position="bottom",
    ),
    href="https://www.linkedin.com/in/snehilvj/",
)

avatars_group = dmc.AvatarsGroup(avatars, total=20, limit=3)

app.layout = dmc.Container(
    [
        html.Div(
            [
                dmc.Title("Avitar Simple Example", order=4, style={"marginBottom": 10}),
                simple_example,
            ],
        ),
        dmc.Space(h=75),
        html.Div(
            [
                dmc.Title("Avitar with Tooltip", order=4, style={"marginBottom": 10}),
                avatar_with_tooltip,
            ],
        ),
        dmc.Space(h=75),
        html.Div(
            [
                dmc.Title("AvatarsGroup", order=4, style={"marginBottom": 10}),
                avatars_group,
            ],
        ),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
