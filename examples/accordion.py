import dash_mantine_components as dmc
from dash import Dash, html
from dash_iconify import DashIconify

app = Dash(__name__)

simple_example = dmc.Accordion(
    children=[
        dmc.AccordionItem(
            "Colors, fonts, shadows and many other parts are customizable to fit your design needs",
            label="Customization",
        ),
        dmc.AccordionItem(
            "Configure temp appearance and behavior with vast amount of settings or overwrite any part of component "
            "styles",
            label="Flexibility",
        ),
    ],
    state={"0": False, "1": True},
)

accordion_with_icons = dmc.Accordion(
    disableIconRotation=True,
    children=[
        dmc.AccordionItem(
            label="Personal Information",
            icon=[
                DashIconify(
                    icon="tabler:user",
                    color=dmc.theme.DEFAULT_COLORS["blue"][6],
                    width=20,
                )
            ],
        ),
        dmc.AccordionItem(
            label="Shipping Address",
            icon=[
                DashIconify(
                    icon="tabler:map-pin",
                    color=dmc.theme.DEFAULT_COLORS["red"][6],
                    width=20,
                )
            ],
        ),
        dmc.AccordionItem(
            label="Confirmation",
            icon=[
                DashIconify(
                    icon="tabler:circle-check",
                    color=dmc.theme.DEFAULT_COLORS["green"][6],
                    width=20,
                )
            ],
        ),
    ],
)

app.layout = dmc.Container(
    [
        html.Div(
            [
                dmc.Title(
                    "Accordion Simple Example", order=4, style={"marginBottom": 10}
                ),
                simple_example,
            ],
        ),
        dmc.Space(h=75),
        html.Div(
            [
                dmc.Title("Accordion with icons", order=4, style={"marginBottom": 10}),
                accordion_with_icons,
            ],
        ),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
