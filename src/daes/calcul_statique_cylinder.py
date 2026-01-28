from daes.geometry import CylinderGeometry, generate_cylinder_geometry
from daes.constraints import generate_cylinder_constraints, generate_cylinder_forces
from daes.solver import solve_system_of_equations
import numpy as np
from dataclasses import dataclass

@dataclass
class FluidProperties:
    density: float
    viscosity: float
    
@dataclass
class ProblemDefinition:
    geometry: CylinderGeometry
    fluid_properties: FluidProperties
    gravity_acceleration: float

def run_calcul_statique_for_cylinder(geometry: CylinderGeometry, gravity_acceleration: float, fluid_density: float, fluid_viscosity: float) -> np.ndarray:
    
    geometry = generate_cylinder_geometry(geometry)
    
    constraints = generate_cylinder_constraints(geometry)
    
    forces = generate_cylinder_forces(geometry=geometry, constraints=constraints, gravity_acceleration=gravity_acceleration, fluid_density=fluid_density, fluid_viscosity=fluid_viscosity)
    
    displacements = solve_system_of_equations(forces, constraints)
    
    return np.ones((3, 3))

def compute_sum_of_list(inputs: list[int]) -> int:
    if len(inputs) != 3:
        raise ValueError("la liste en entrée doit contenir 3 éléments qui correspondent aux coordonnées x, y, z")
    sum = inputs[0] + inputs[1] + inputs[2]
    return sum

def compute_sum_of_list2(inputs: list[int]) -> int:
    try:
        sum = inputs[0] + inputs[1] + inputs[2]
        return sum
    except:
        raise ValueError("la liste en entrée doit contenir 3 éléments qui correspondent aux coordonnées x, y, z")


        
def main() -> None:
    output = compute_sum_of_list([1, 2, 3])
    print("output:", output)
    

    
