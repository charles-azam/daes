from dataclasses import dataclass

@dataclass
class Force:
    x: float
    y: float
    z: float


def compute_force_gravity(mass: float, gravity_acceleration: float) -> Force:
    return Force(x=0, y=0, z=-mass * gravity_acceleration)

def compute_force_drag(velocity: float, density: float, viscosity: float) -> Force:
    return Force(x=0, y=0, z=-0.5 * density * velocity**2 * viscosity)

import numpy as np
def compute_sum_of_forces(force_1: np.ndarray, force_2: np.ndarray) -> np.ndarray:
    assert force_1.shape == force_2.shape
    return force_1 + force_2