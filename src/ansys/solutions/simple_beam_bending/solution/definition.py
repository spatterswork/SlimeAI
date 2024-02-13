# ©2023, ANSYS Inc. Unauthorized use, distribution or duplication is prohibited.

"""Solution definition module."""


from ansys.saf.glow.solution import Solution, StepsModel

from ansys.solutions.simple_beam_bending.solution.compute_step import ComputeStep
from ansys.solutions.simple_beam_bending.solution.context_step import ContextStep


class Steps(StepsModel):
    """Workflow definition."""

    context_step: ContextStep
    compute_step: ComputeStep


class Simple_Beam_BendingSolution(Solution):
    """Solution definition."""

    display_name: str = "Simple Beam Bending"
    steps: Steps
