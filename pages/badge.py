import dash

from lib.code_and_show import example_app

filename = __name__.split("pages.")[1]

dash.register_page(
    __name__,
    title=f"Dash Mantine Components example - {filename}",
    dmc_docs_path=f"/components/{filename}",
)

# displayed in a dcc.Markdown component under the example app
notes = f"""
For more information on how to configure the dmc.Badge, see the dmc-docs
[Reference](https://www.dash-mantine-components.com/components/{filename}#keyword-arguments)

"""


layout = example_app(filename, notes=notes)
