"""
Creates an app used by script to update the images.  Each page contains example app only with no navigation or headers.
Start this app, then run update_images_all.py or update_images_missing.py
"""


import dash
import dash_mantine_components as dmc
from lib.code_and_show import example_app
from lib.utils import file_names

from lib.utils import example_apps

app = dash.Dash(
    __name__,
    use_pages=True,
    pages_folder="",
)

for k in example_apps:
    # Prepend to layout IDs recursively in-place
    new_callback_map = example_apps[k].callback_map
    new_callback_list = example_apps[k]._callback_list

    app.callback_map.update(new_callback_map)
    app._callback_list.extend(new_callback_list)

for page in file_names:
    dash.register_page(
        page,
        layout=example_app(page, show_code=False),
    )

app.layout = dmc.MantineProvider(
    id="theme-provider",
    theme={
        "colorScheme": "dark",
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
    children=dmc.Container(
        dash.page_container, fluid=True, style={"marginTop": "4rem"}
    ),
)


if __name__ == "__main__":
    app.run_server(debug=False)
