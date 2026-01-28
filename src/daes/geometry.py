import numpy as np
from dataclasses import dataclass, field
@dataclass
class CylinderGeometry:
    height: list[float] = field(default_factory=lambda: [])
    radius: list[float] = field(default_factory=lambda: [0.5, 1.0, 1.5])
    
    def volume(self) -> float:
        return np.pi * self.radius**2 * self.height
    
def generate_cylinder_geometry(cylinder_geometry: CylinderGeometry) -> np.ndarray:
    return np.array([cylinder_geometry.height, cylinder_geometry.radius])