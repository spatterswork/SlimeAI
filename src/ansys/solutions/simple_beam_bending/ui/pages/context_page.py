# ©2023, ANSYS Inc. Unauthorized use, distribution or duplication is prohibited.

"""Frontend of the first step."""

import base64
import os
from pathlib import Path

import dash_bootstrap_components as dbc
from dash_extensions.enrich import dcc, html

from ansys.solutions.simple_beam_bending.solution.context_step import ContextStep


def layout(step: ContextStep):
    """Layout of the first step UI."""

    sketch = base64.b64encode(
        open(os.path.join(Path(__file__).absolute().parent.parent, "assets", "images", "reflector_image.png"), "rb").read()
    )

    return html.Div(
        dbc.Container(
            [
                html.H1("Parabolic Reflector - Bezel Check", className="display-3", style={"font-size": "35px"}),

                html.Hr(className="my-2"),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Row(
                                    [
                                        
                                        dcc.Markdown(
                                            """
                                          

                                            Model to predict what range of focal lengths can fit within the bezel opening and whether they can pass the regulations required minimum flux
 
                                            """,
                                            mathjax=True,
                                            className="lead",
                                            style={
                                                "textAlign": "center",
                                                "marginLeft": "auto",
                                                "marginRight": "auto",
                                                "font-size": "18px",
                                            },
                                        ),
                                        html.Br(),
                                        
                                    ]
                                )
                            ],
                            width=7,
                        ),
                        dbc.Col(
                            [
                                dbc.Row(
                                    [
                                        
                                        html.Br(),
                                        dbc.Card(
                                            [
                                                dbc.CardImg(
                                                    src="data:image/png;base64,{}".format(sketch.decode()),
                                                ),
                                                dbc.CardFooter("Reflector with bezel contour and source axis system"),
                                            ],
                                            style={"width": "20rem"},
                                        ),
                                    ]
                                )
                            ],
                            width=4,
                        ),
                    ]
                ),
            ],
            fluid=True,
            className="py-3",
        ),
        className="p-3 bg-light rounded-3",
    )
