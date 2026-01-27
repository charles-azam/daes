import numpy as np


def generate_cylinder_geometry(cylinder_height: float, cylinder_radius: float) -> np.ndarray:
    return np.array([cylinder_height, cylinder_radius])