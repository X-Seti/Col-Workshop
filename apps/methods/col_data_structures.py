#this belongs in methods/col_data_structures.py - Version: 1
# X-Seti - December17 2025 - Col Workshop - COL Data Structures

"""
COL Data Structures - Based on GTA Wiki specification
Pure data classes for COL file format (COL1, COL2, COL3)
Reference: https://gta.fandom.com/wiki/Collision_File
"""

from typing import List, Tuple
from enum import IntEnum

##Classes list -
# BoundingBox
# COLBox
# COLFace
# COLFaceGroup
# COLModel
# COLSphere
# COLVersion
# COLVertex
# Vector3

class Vector3: #vers 1
    """3D Vector - Used throughout COL structures"""
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    
    def __repr__(self):
        return f"Vector3({self.x:.3f}, {self.y:.3f}, {self.z:.3f})"
    
    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"


class COLVersion(IntEnum): #vers 1
    """COL file format versions"""
    COL_1 = 1  # GTA III, Vice City - COLL signature
    COL_2 = 2  # GTA SA PS2 - COL2 signature  
    COL_3 = 3  # GTA SA PC/Xbox - COL3 signature
    COL_4 = 4  # Unused/planned version


class BoundingBox: #vers 1
    """Axis-aligned bounding box - Structure varies by version"""
    def __init__(self):
        self.min = Vector3(-1.0, -1.0, -1.0)
        self.max = Vector3(1.0, 1.0, 1.0)
        self.center = Vector3(0.0, 0.0, 0.0)
        self.radius = 1.0
    
    def __repr__(self):
        return f"BoundingBox(center={self.center}, radius={self.radius:.2f})"


class COLSphere: #vers 1
    """Collision sphere - 20 bytes total
    
    Structure (from GTA Wiki):
    COL1: radius(4) + center(12) + surface(4)
    COL2/3: center(12) + radius(4) + surface(4)
    """
    def __init__(self):
        self.center = Vector3()
        self.radius = 1.0
        self.material = 0  # Surface material ID
        self.flags = 0     # Surface flags
    
    def __repr__(self):
        return f"COLSphere(center={self.center}, r={self.radius:.2f}, mat={self.material})"


class COLBox: #vers 1
    """Collision box (axis-aligned) - 28 bytes total
    
    Structure: min(12) + max(12) + surface(4)
    """
    def __init__(self):
        self.min_point = Vector3()
        self.max_point = Vector3()
        self.material = 0  # Surface material ID
        self.flags = 0     # Surface flags (COL1 only)
    
    def __repr__(self):
        return f"COLBox(min={self.min_point}, max={self.max_point}, mat={self.material})"


class COLVertex: #vers 1
    """Mesh vertex
    
    Size varies by version:
    COL1: 12 bytes (float[3])
    COL2/3: 6 bytes (int16[3]) - divide by 128.0 to get float
    """
    def __init__(self, position: Vector3 = None):
        self.position = position if position else Vector3()
    
    def __repr__(self):
        return f"COLVertex({self.position})"


class COLFace: #vers 1
    """Mesh face (triangle)
    
    Size varies by version:
    COL1: 16 bytes - indices(3x4) + material(2) + light(2) + flags(4) + padding(2)
    COL2/3: 8 bytes - indices(3x2) + material(1) + light(1)
    """
    def __init__(self):
        self.a = 0  # Vertex index 1
        self.b = 0  # Vertex index 2
        self.c = 0  # Vertex index 3
        self.material = 0  # Surface material ID
        self.light = 0     # Light intensity (0-255, COL2/3 only)
        self.flags = 0     # Face flags (COL1 only)
    
    @property
    def vertex_indices(self) -> Tuple[int, int, int]:
        """Get vertex indices as tuple"""
        return (self.a, self.b, self.c)
    
    def __repr__(self):
        return f"COLFace(indices=({self.a}, {self.b}, {self.c}), mat={self.material})"


class COLFaceGroup: #vers 1
    """Face group for optimization (COL2/3 only) - 28 bytes
    
    Groups faces by bounding box for faster collision detection
    """
    def __init__(self):
        self.min = Vector3()
        self.max = Vector3()
        self.start_face = 0  # First face index in group
        self.end_face = 0    # Last face index in group
    
    def __repr__(self):
        face_count = self.end_face - self.start_face + 1
        return f"COLFaceGroup(faces={face_count}, range={self.start_face}-{self.end_face})"


class COLModel: #vers 1
    """Complete COL model - Single collision model in COL file"""
    def __init__(self):
        # Header data
        self.signature = b'COLL'
        self.version = COLVersion.COL_1
        self.file_size = 0
        self.name = ""
        self.model_id = 0
        
        # Bounding data
        self.bounding_box = BoundingBox()
        
        # Collision primitives
        self.spheres: List[COLSphere] = []
        self.boxes: List[COLBox] = []
        
        # Mesh data
        self.vertices: List[COLVertex] = []
        self.faces: List[COLFace] = []
        self.face_groups: List[COLFaceGroup] = []  # COL2/3 only
        
        # Shadow mesh (COL3 only)
        self.shadow_vertices: List[COLVertex] = []
        self.shadow_faces: List[COLFace] = []
        
        # Flags (COL2/3)
        self.flags = 0
        self.has_face_groups = False
        self.has_shadow_mesh = False
    
    def __repr__(self):
        return (f"COLModel(name='{self.name}', version={self.version.name}, "
                f"S:{len(self.spheres)} B:{len(self.boxes)} "
                f"V:{len(self.vertices)} F:{len(self.faces)})")


# Export all classes
__all__ = [
    'Vector3',
    'COLVersion',
    'BoundingBox',
    'COLSphere',
    'COLBox',
    'COLVertex',
    'COLFace',
    'COLFaceGroup',
    'COLModel'
]
