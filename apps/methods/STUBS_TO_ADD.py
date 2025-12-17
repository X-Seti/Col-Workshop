# ===== TEMPORARY STUBS - Add after line 46 in col_workshop.py =====
# These are placeholders until we rebuild the parser from GTA Wiki spec
# Will be replaced by: from apps.methods.col_data_structures import *

class Vector3:
    """Temporary 3D vector stub"""
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    
    def __repr__(self):
        return f"Vector3({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"

class COLVersion:
    """COL format version enum"""
    COL_1 = 1  # GTA III/VC - COLL signature
    COL_2 = 2  # GTA SA PS2 - COL2 signature
    COL_3 = 3  # GTA SA PC/Xbox - COL3 signature
    
    def __init__(self, value):
        self.value = value
        if value == 1:
            self.name = "COL1"
        elif value == 2:
            self.name = "COL2"
        elif value == 3:
            self.name = "COL3"
        else:
            self.name = f"COL{value}"

class COLModel:
    """Temporary COL model stub"""
    def __init__(self):
        self.name = "Unknown"
        self.version = COLVersion(1)
        self.model_id = 0
        self.spheres = []
        self.boxes = []
        self.vertices = []
        self.faces = []
        self.bounding_box = None

class COLFile:
    """Temporary COL file stub - Will be replaced by proper parser"""
    def __init__(self, file_path=None):
        self.file_path = file_path
        self.models = []
        self.is_loaded = False
        self.load_error = None
    
    def load_from_file(self, file_path):
        """Stub load - Parser being rebuilt from GTA Wiki spec"""
        self.load_error = "Parser not yet implemented - Use new methods/col_parser.py"
        return False
    
    def save_to_file(self, file_path):
        """Stub save - Writer being rebuilt"""
        return False

# ===== END TEMPORARY STUBS =====
