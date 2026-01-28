from daes.calcul_statique_cylinder import run_calcul_statique_for_cylinder
from daes.geometry import CylinderGeometry
import numpy as np

def test_run_calcul_statique_for_cylinder() -> None:
    geometry = CylinderGeometry(height=[1.0, 2.0, 3.0], radius=[0.5, 1.0, 1.5])
    gravity_acceleration = 9.81
    fluid_density = 1000
    fluid_viscosity = 0.001
    displacements = run_calcul_statique_for_cylinder(geometry, gravity_acceleration, fluid_density, fluid_viscosity)
    assert displacements.shape == (3, 3)
    assert np.allclose(displacements, np.ones((3, 3)))
    
    assert False




if __name__ == "__main__":
    test_run_calcul_statique_for_cylinder()