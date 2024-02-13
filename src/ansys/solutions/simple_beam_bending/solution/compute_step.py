# ©2023, ANSYS Inc. Unauthorized use, distribution or duplication is prohibited.

"""Backend of the first step."""


from typing import List

from ansys.saf.glow.solution import StepModel, StepSpec, transaction

from ansys.solutions.simple_beam_bending.logic.beam_deflection import compute_beam_deflection


class ComputeStep(StepModel):
    """Step definition of the first step."""

    length_a: float = 1000  # mm
    length_b: float = 1000  # mm
    diameter: float = 50  # mm
    elasticity_modulus: float = 210e3  # MPa
    load: float = 10e3  # N
    nbr_of_pts: int = 100
    deflection: List = []  # [[mm], [mm]]

    @transaction(
        self=StepSpec(
            download=["length_a", "length_b", "diameter", "elasticity_modulus", "load", "nbr_of_pts"],
            upload=["deflection"],
        )
    )
    def compute_beam_deflection(self) -> None:
        """Method to compute the deflection of a simply supported beam."""
        self.deflection = compute_beam_deflection(
            self.length_a, self.length_b, self.diameter, self.elasticity_modulus, self.load, n=self.nbr_of_pts
        )
