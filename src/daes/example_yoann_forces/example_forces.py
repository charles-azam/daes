from dataclasses import dataclass
import numpy as np
from typing import Any

@dataclass
class Force:
    x: float
    y: float
    z: float
    
class Forces:

    @staticmethod
    def compute_force_gravity(mass: float, gravity_acceleration: float) -> Force:
        return Force(x=0, y=0, z=-mass * gravity_acceleration)

    @staticmethod
    def compute_force_drag(velocity: float, density: float, viscosity: float) -> Force:
        return Force(x=0, y=0, z=-0.5 * density * velocity**2 * viscosity)
    

def solver(times: np.ndarray):
    for time in times:
        gravity = Forces.compute_force_gravity(mass, gravity_acceleration)
        drag = Forces.compute_force_drag(velocity, density, viscosity)
        force = gravity + drag
        velocity = velocity + force * time
    pass


    
    
## version ++

from abc import ABC, abstractmethod

class GenerateurForce(ABC):
    
    @abstractmethod
    def generate(self, time: float, velocity: Velocity
                 ) -> Force:
        raise NotImplementedError
    
class GenerateurForceGravity(GenerateurForce):
    def generate(self, time: float, velocity: Velocity
                 ) -> Force:
        return Force(x=0, y=0, z=-mass * gravity_acceleration)
    
class GenerateurForceDrag(GenerateurForce):
    def generate(self, time: float, velocity: Velocity
                 ) -> Force:
        return Force(x=0, y=0, z=-0.5 * density * velocity**2 * viscosity)
    
def solver(times: np.ndarray, generateur_forces: list[GenerateurForce]):
    for time in times:
        for generateur_force in generateur_forces:
            force = generateur_force.generate(time, velocity=velocity)
    pass

if __name__ == "__main__":
    times = np.linspace(0, 1, 100)
    generateur_forces = [GenerateurForceGravity(mass, gravity_acceleration), GenerateurForceDrag(density, viscosity)]
    solver(times, generateur_forces)