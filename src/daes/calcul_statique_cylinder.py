from daes.geometry import generate_cylinder_geometry
from daes.constraints import generate_cylinder_constraints, generate_cylinder_forces
from daes.solver import solve_system_of_equations
import numpy as np


def run_calcul_statique_for_cylinder(cylinder_height: float, cylinder_radius: float, gravity_acceleration: float, fluid_density: float, fluid_viscosity: float) -> None:
    
    geometry = generate_cylinder_geometry(cylinder_height, cylinder_radius)
    
    constraints = generate_cylinder_constraints(geometry)
    
    forces = generate_cylinder_forces(geometry, constraints, gravity_acceleration, fluid_density, fluid_viscosity)
    
    displacements = solve_system_of_equations(forces, constraints)
    
    return displacements

def save_displacements_to_images(displacements: np.ndarray) -> None:
    ...
    
def main() -> None:
    displacements = run_calcul_statique_for_cylinder(1.0, 0.5, 9.81, 1000, 0.001)
    save_displacements_to_images(displacements)

    
if __name__ == "__main__":
    main()