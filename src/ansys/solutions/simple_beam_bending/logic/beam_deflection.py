# ©2023, ANSYS Inc. Unauthorized use, distribution or duplication is prohibited.

import numpy as np


def compute_beam_deflection(a: float, b: float, d: float, E: float, p: float, n: int = 100) -> list:
    """Computes the deflection of a simply supported beam at ends with concentrated load P. The
    beam has a circular section of diameter d.

    Parameters
    ----------
    a : float
        X coordinate of the load P with respect to the left-hand support (mm).
    b : float
        X coordinate of the load P with respect to the right-hand support (mm).
    d: float
        Diameter of the beam section (mm).
    E: float
        Elastic modulus of the material the beam is made of (MPa).
    p : float
        Amplitude of the vertical load P (N).
    n: int
        Number of points along the beam axis on which the deflection is computed.

    Returns
    -------
    list
        X coordinates of the beam centerline.
    list
        Vertical displacement of the beam centerline evaluated for each `nx` point.
    """

    # Total beam length (mm)
    l = a + b

    # Moment of inertia (mm^4)
    I3 = np.pi * d**4 / 64

    # Space discretization
    x1 = np.linspace(0, a + b, n)

    # Initialize the deflection (mm)
    u2 = np.zeros_like(x1)

    # Compute deflection (mm)
    for i, x in enumerate(x1):
        if x <= a:
            u2[i] = -p * b * x * (l**2 - x**2 - b**2) / (6 * l * E * I3)
        else:
            u2[i] = -p * b * (l / b * (x - a) ** 3 + (l**2 - b**2) * x - x**3) / (6 * l * E * I3)

    return [x1.tolist(), u2.tolist()]
