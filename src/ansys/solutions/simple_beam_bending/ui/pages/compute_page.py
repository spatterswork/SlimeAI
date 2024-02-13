# ©2023, ANSYS Inc. Unauthorized use, distribution or duplication is prohibited.

"""Frontend of the first step."""

import base64
import os
from pathlib import Path

from ansys.saf.glow.client.dashclient import DashClient, callback
from ansys.solutions.dash_components.table import InputRow
import dash_bootstrap_components as dbc
from dash_extensions.enrich import Input, Output, State, dcc, html

from ansys.solutions.simple_beam_bending.solution.compute_step import ComputeStep
from ansys.solutions.simple_beam_bending.solution.definition import Simple_Beam_BendingSolution


def layout(step: ComputeStep):
    """Layout of the first step UI."""

    sketch = base64.b64encode(
        open(os.path.join(Path(__file__).absolute().parent.parent, "assets", "images", "reflector_image.png"), "rb").read()
    )

    return html.Div(
        [
            dcc.Markdown("""#### Compute optimal reflector parameters """, className="display-3"),

            html.Hr(className="my-2"),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(
                        [

                            dcc.Upload(html.Button('Upload File')),

                            html.Br(),
                            html.Div(
                                
                                dbc.Button(
                                    "Compute",
                                    id="compute_deflection",
                                    disabled=False,
                                    style={
                                        "display": "flex",
                                        "justify-content": "center",
                                        "align-items": "center",
                                        "fontSize": "100%",
                                        "background-color": "rgba(0, 0, 0, 1)",
                                        "border-color": "rgba(0, 0, 0, 1)",
                                        "height": "30px",
                                    },
                                ),
                                className="d-grid gap-2 col-5 mx-auto",
                            ),
                        ],
                        width=6,
                    ),
                    dbc.Col(
                        [
                            html.Div(
                                dbc.Card(
                                    [
                                        dbc.CardImg(
                                            src="data:image/png;base64,{}".format(sketch.decode()),
                                        ),
                                        dbc.CardFooter("Reflector with bezel contour and source axis system"),
                                    ],
                                    style={"width": "20rem"},
                                ),
                                style={
                                    "width": "100%",
                                    "display": "flex",
                                    "align-items": "center",
                                    "justify-content": "center",
                                },
                            ),
                            
                        ],
                        width=6,
                    ),
                ]
            ),
            dcc.Loading(
                type="circle",
                fullscreen=True,
                color="#ffb71b",
                style={
                    "background-color": "rgba(55, 58, 54, 0.1)",
                },
                children=html.Div(id="wait_for_completion"),
            ),
        ]
    )


@callback(
    Output("deflection_graph", "figure"),
    Output("wait_for_completion", "children"),
    Input("compute_deflection", "n_clicks"),
    State("length_a", "value"),
    State("length_b", "value"),
    State("diameter", "value"),
    State("elasticity_modulus", "value"),
    State("load", "value"),
    State("nbr_of_pts", "value"),
    State("url", "pathname"),
    State("deflection_graph", "figure"),
    prevent_initial_call=True,
)
def compute_beam_deflection(
    n_clicks, length_a, length_b, diameter, elasticity_modulus, load, nbr_of_pts, pathname, figure
):
    """Callback function to trigger the computation."""
    project = DashClient[Simple_Beam_BendingSolution].get_project(pathname)
    step = project.steps.compute_step
    step.length_a = length_a
    step.length_b = length_b
    step.diameter = diameter
    step.elasticity_modulus = elasticity_modulus
    step.load = load
    step.nbr_of_pts = nbr_of_pts
    step.compute_beam_deflection()

    figure["data"][1]["x"] = step.deflection[0]
    figure["data"][1]["y"] = step.deflection[1]

    return figure, True
