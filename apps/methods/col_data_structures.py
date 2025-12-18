#this belongs in methods/col_data_structures.py - Version: 1
# X-Seti - December18 2025 - Col Workshop - COL Data Structures
"""
COL Data Structures - Pure data classes for collision files
Clean implementation for COL format versions 1, 2, 3, 4
"""

from enum import Enum
from dataclasses import dataclass
from typing import List, Tuple

##Classes -
# BoundingBox
# COLBox
# COLFace
# COLFaceGroup
# COLMaterial
# COLModel
# COLSphere
# COLVersion
# COLVertex
# Vector3

class Vector3:
    """3D vector with x, y, z components"""
    
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"
    
    def __repr__(self):
        return f"Vector3({self.x}, {self.y}, {self.z})"


class BoundingBox:
    """Axis-aligned bounding box"""
    
    def __init__(self):
        self.min = Vector3(-1.0, -1.0, -1.0)
        self.max = Vector3(1.0, 1.0, 1.0)
        self.center = Vector3(0.0, 0.0, 0.0)
        self.radius = 1.0
    
    def __str__(self):
        return f"BoundingBox(min={self.min}, max={self.max}, r={self.radius:.2f})"


class COLVersion(Enum):
    """COL file format versions"""
    COL_1 = 1  # GTA III
    COL_2 = 2  # GTA Vice City
    COL_3 = 3  # GTA San Andreas
    COL_4 = 4  # Extended


class COLMaterial:
    """Material/surface properties"""
    
    def __init__(self, material_id: int = 0, flags: int = 0):
        self.material_id = material_id
        self.flags = flags
    
    def __str__(self):
        return f"Material({self.material_id})"


class COLSphere:
    """Collision sphere"""
    
    def __init__(self, center: Vector3, radius: float, material: COLMaterial):
        self.center = center
        self.radius = radius
        self.material = material
    
    def __str__(self):
        return f"Sphere(c={self.center}, r={self.radius:.2f})"


class COLBox:
    """Collision box (axis-aligned)"""
    
    def __init__(self, min_point: Vector3, max_point: Vector3, material: COLMaterial):
        self.min_point = min_point
        self.max_point = max_point
        self.material = material
    
    def __str__(self):
        return f"Box(min={self.min_point}, max={self.max_point})"


class COLVertex:
    """Mesh vertex"""
    
    def __init__(self, position: Vector3):
        self.position = position
    
    def __str__(self):
        return f"Vertex({self.position})"


class COLFace:
    """Mesh face (triangle)"""
    
    def __init__(self, vertex_indices: Tuple[int, int, int], material: COLMaterial, light: int = 0):
        self.vertex_indices = vertex_indices
        self.material = material
        self.light = light
    
    def __str__(self):
        return f"Face({self.vertex_indices}, mat={self.material.material_id})"


class COLFaceGroup:
    """Face group for COL2/COL3"""
    
    def __init__(self):
        self.faces: List[COLFace] = []
        self.material = COLMaterial()


class COLModel:
    """Complete COL collision model"""
    
    def __init__(self):
        self.name = ""
        self.model_id = 0
        self.version = COLVersion.COL_1
        self.bounding_box = BoundingBox()
        
        # Collision elements
        self.spheres: List[COLSphere] = []
        self.boxes: List[COLBox] = []
        self.vertices: List[COLVertex] = []
        self.faces: List[COLFace] = []
        self.face_groups: List[COLFaceGroup] = []
        
        # Status flags
        self.has_sphere_data = False
        self.has_box_data = False
        self.has_mesh_data = False
    
    def get_stats(self) -> str:
        return f"{self.name}: S:{len(self.spheres)} B:{len(self.boxes)} V:{len(self.vertices)} F:{len(self.faces)}"
    
    def update_flags(self):
        """Update status flags"""
        self.has_sphere_data = len(self.spheres) > 0
        self.has_box_data = len(self.boxes) > 0
        self.has_mesh_data = len(self.vertices) > 0 and len(self.faces) > 0


# Export all classes
__all__ = [
    'Vector3',
    'BoundingBox',
    'COLVersion',
    'COLMaterial',
    'COLSphere',
    'COLBox',
    'COLVertex',
    'COLFace',
    'COLFaceGroup',
    'COLModel'
]
