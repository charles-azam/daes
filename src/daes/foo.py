from dataclasses import dataclass, field
import numpy as np

@dataclass
class CylinderGeometry:
    height: list[float] = field(default_factory=lambda: [])
    radius: list[float] = field(default_factory=lambda: [0.5, 1.0, 1.5])
    
    def volume(self) -> float:
        return np.pi * self.radius**2 * self.height
    
@dataclass
class CubeGeometry:
    side_length: list[float] = field(default_factory=lambda: [])
    
    def volume(self) -> float:
        return self.side_length**3

@dataclass
class SphereGeometry:
    radius: list[float] = field(default_factory=lambda: [])
    
    def volume(self) -> float:
        return 4/3 * np.pi * self.radius**3

def compute_volume_of_cylinder(geometry: CylinderGeometry) -> float:
    return np.pi * geometry.radius**2 * geometry.height

cylinder_geometry = CylinderGeometry(height=[1.0, 2.0, 3.0], radius=[0.5, 1.0, 1.5])

volume = compute_volume_of_cylinder(cylinder_geometry)
volume = cylinder_geometry.volume()