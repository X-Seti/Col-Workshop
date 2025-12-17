#this belongs in methods/col_parser.py - Version: 1
# X-Seti - December17 2025 - Col Workshop - COL File Parser

"""
COL Parser - Complete COL file parsing (COL1, COL2, COL3)
Based on GTA Wiki specification: https://gta.fandom.com/wiki/Collision_File

Supports:
- COL1 (GTA III, Vice City) - COLL signature
- COL2 (GTA SA PS2) - COL2 signature  
- COL3 (GTA SA PC/Xbox) - COL3 signature

Key differences:
- COL1: float vertices, uint32 face indices, no compression
- COL2/3: int16 vertices (÷128), uint16 face indices, face groups
- COL3: Adds shadow mesh
"""

import struct
from typing import List, Tuple, Optional
from pathlib import Path

from col_data_structures import (
    Vector3, COLVersion, BoundingBox, COLSphere, COLBox,
    COLVertex, COLFace, COLFaceGroup, COLModel
)

##Methods list -
# parse_col_file
# parse_col_model
# _parse_col1_header
# _parse_col23_header
# _parse_col1_body
# _parse_col23_body
# _parse_bounding_box_col1
# _parse_bounding_box_col23
# _parse_spheres
# _parse_boxes
# _parse_vertices_col1
# _parse_vertices_col23
# _parse_faces_col1
# _parse_faces_col23
# _parse_face_groups
# _parse_shadow_mesh
# _fixed_to_float
# _validate_signature

class COLParser: #vers 1
    """COL file parser - handles all COL versions"""
    
    def __init__(self, debug: bool = False):
        self.debug = debug
        self.errors = []
    
    def parse_col_file(self, file_path: str) -> Tuple[List[COLModel], List[str]]: #vers 1
        """Parse complete COL file - may contain multiple models
        
        Args:
            file_path: Path to COL file
            
        Returns:
            Tuple of (models list, errors list)
        """
        try:
            with open(file_path, 'rb') as f:
                data = f.read()
            
            if self.debug:
                print(f"[COL Parser] Loading {Path(file_path).name} ({len(data)} bytes)")
            
            models = []
            offset = 0
            model_index = 0
            
            # Parse all models in file
            while offset < len(data):
                if offset + 8 > len(data):
                    break
                
                # Check for valid signature
                sig = data[offset:offset+4]
                if sig not in [b'COLL', b'COL\x02', b'COL\x03', b'COL\x04']:
                    # End of valid models
                    break
                
                model, consumed = self.parse_col_model(data, offset)
                
                if model is None or consumed == 0:
                    self.errors.append(f"Failed to parse model at offset {offset}")
                    break
                
                models.append(model)
                offset += consumed
                model_index += 1
                
                if self.debug:
                    print(f"[COL Parser] Model {model_index}: {model}")
                
                # Safety limit
                if model_index > 200:
                    self.errors.append("Safety limit: 200 models parsed")
                    break
            
            if self.debug:
                print(f"[COL Parser] Loaded {len(models)} models")
            
            return models, self.errors
            
        except Exception as e:
            self.errors.append(f"File read error: {e}")
            return [], self.errors
    
    def parse_col_model(self, data: bytes, offset: int) -> Tuple[Optional[COLModel], int]: #vers 1
        """Parse single COL model from data
        
        Args:
            data: Complete file data
            offset: Current offset in data
            
        Returns:
            Tuple of (COLModel or None, bytes consumed)
        """
        try:
            start_offset = offset
            
            # Read signature to determine version
            if offset + 4 > len(data):
                return None, 0
            
            signature = data[offset:offset+4]
            
            # Determine version
            if signature == b'COLL':
                version = COLVersion.COL_1
            elif signature == b'COL\x02':
                version = COLVersion.COL_2
            elif signature == b'COL\x03':
                version = COLVersion.COL_3
            elif signature == b'COL\x04':
                version = COLVersion.COL_4
            else:
                return None, 0
            
            # Parse based on version
            if version == COLVersion.COL_1:
                model, offset = self._parse_col1_model(data, offset)
            else:
                model, offset = self._parse_col23_model(data, offset, version)
            
            if model:
                consumed = offset - start_offset
                return model, consumed
            else:
                return None, 0
                
        except Exception as e:
            self.errors.append(f"Model parse error at offset {offset}: {e}")
            return None, 0
    
    def _parse_col1_model(self, data: bytes, offset: int) -> Tuple[Optional[COLModel], int]: #vers 1
        """Parse COL1 model (GTA III, Vice City)"""
        try:
            model = COLModel()
            model.version = COLVersion.COL_1
            
            # Parse header (40 bytes)
            model, offset = self._parse_col1_header(data, offset, model)
            if not model:
                return None, offset
            
            # Parse body
            model, offset = self._parse_col1_body(data, offset, model)
            
            return model, offset
            
        except Exception as e:
            self.errors.append(f"COL1 parse error: {e}")
            return None, offset
    
    def _parse_col23_model(self, data: bytes, offset: int, version: COLVersion) -> Tuple[Optional[COLModel], int]: #vers 1
        """Parse COL2/COL3 model (GTA SA)"""
        try:
            model = COLModel()
            model.version = version
            
            # Parse header (with offsets)
            model, offset = self._parse_col23_header(data, offset, model)
            if not model:
                return None, offset
            
            # Parse body using offsets
            model = self._parse_col23_body(data, model)
            
            # Calculate consumed bytes from file_size
            return model, offset
            
        except Exception as e:
            self.errors.append(f"COL2/3 parse error: {e}")
            return None, offset
    
    def _parse_col1_header(self, data: bytes, offset: int, model: COLModel) -> Tuple[Optional[COLModel], int]: #vers 1
        """Parse COL1 header - 40 bytes total"""
        try:
            # Signature (4 bytes)
            model.signature = data[offset:offset+4]
            offset += 4
            
            # File size (4 bytes)
            model.file_size = struct.unpack('<I', data[offset:offset+4])[0]
            offset += 4
            
            # Model name (22 bytes, null-terminated)
            name_bytes = data[offset:offset+22]
            model.name = name_bytes.split(b'\x00')[0].decode('ascii', errors='ignore')
            offset += 22
            
            # Model ID (2 bytes)
            model.model_id = struct.unpack('<H', data[offset:offset+2])[0]
            offset += 2
            
            # Bounding box (40 bytes) - COL1 structure
            model.bounding_box, offset = self._parse_bounding_box_col1(data, offset)
            
            return model, offset
            
        except Exception as e:
            self.errors.append(f"COL1 header parse error: {e}")
            return None, offset
    
    def _parse_col23_header(self, data: bytes, offset: int, model: COLModel) -> Tuple[Optional[COLModel], int]: #vers 1
        """Parse COL2/COL3 header - variable size with offsets"""
        try:
            start_offset = offset
            
            # Signature (4 bytes)
            model.signature = data[offset:offset+4]
            offset += 4
            
            # File size (4 bytes) - relative to after fourcc
            model.file_size = struct.unpack('<I', data[offset:offset+4])[0]
            offset += 4
            
            # Model name (22 bytes)
            name_bytes = data[offset:offset+22]
            model.name = name_bytes.split(b'\x00')[0].decode('ascii', errors='ignore')
            offset += 22
            
            # Model ID (2 bytes)
            model.model_id = struct.unpack('<H', data[offset:offset+2])[0]
            offset += 2
            
            # Bounding box (40 bytes) - COL2/3 structure
            model.bounding_box, offset = self._parse_bounding_box_col23(data, offset)
            
            # Counts (8 bytes)
            num_spheres = struct.unpack('<H', data[offset:offset+2])[0]
            offset += 2
            num_boxes = struct.unpack('<H', data[offset:offset+2])[0]
            offset += 2
            num_faces = struct.unpack('<H', data[offset:offset+2])[0]
            offset += 2
            num_wheels = struct.unpack('<B', data[offset:offset+1])[0]  # Unused
            offset += 1
            padding = struct.unpack('<B', data[offset:offset+1])[0]
            offset += 1
            
            # Flags (4 bytes)
            model.flags = struct.unpack('<I', data[offset:offset+4])[0]
            offset += 4
            
            model.has_face_groups = bool(model.flags & 8)
            model.has_shadow_mesh = bool(model.flags & 16) and model.version == COLVersion.COL_3
            
            # Offsets (6 * 4 = 24 bytes) - relative to after fourcc (start_offset + 4)
            base_offset = start_offset + 4
            
            offset_spheres = struct.unpack('<I', data[offset:offset+4])[0]
            offset += 4
            offset_boxes = struct.unpack('<I', data[offset:offset+4])[0]
            offset += 4
            offset_suspension = struct.unpack('<I', data[offset:offset+4])[0]  # Unused
            offset += 4
            offset_vertices = struct.unpack('<I', data[offset:offset+4])[0]
            offset += 4
            offset_faces = struct.unpack('<I', data[offset:offset+4])[0]
            offset += 4
            offset_planes = struct.unpack('<I', data[offset:offset+4])[0]  # Unused
            offset += 4
            
            # COL3 shadow mesh offsets
            offset_shadow_vertices = 0
            offset_shadow_faces = 0
            num_shadow_faces = 0
            
            if model.version == COLVersion.COL_3:
                num_shadow_faces = struct.unpack('<I', data[offset:offset+4])[0]
                offset += 4
                offset_shadow_vertices = struct.unpack('<I', data[offset:offset+4])[0]
                offset += 4
                offset_shadow_faces = struct.unpack('<I', data[offset:offset+4])[0]
                offset += 4
            
            # Store offsets and counts for body parsing
            model._parse_data = {
                'base_offset': base_offset,
                'num_spheres': num_spheres,
                'num_boxes': num_boxes,
                'num_faces': num_faces,
                'num_shadow_faces': num_shadow_faces,
                'offset_spheres': offset_spheres,
                'offset_boxes': offset_boxes,
                'offset_vertices': offset_vertices,
                'offset_faces': offset_faces,
                'offset_shadow_vertices': offset_shadow_vertices,
                'offset_shadow_faces': offset_shadow_faces
            }
            
            return model, offset
            
        except Exception as e:
            self.errors.append(f"COL2/3 header parse error: {e}")
            return None, offset
    
    def _parse_col1_body(self, data: bytes, offset: int, model: COLModel) -> Tuple[COLModel, int]: #vers 1
        """Parse COL1 body - sequential data"""
        try:
            # Number of spheres (4 bytes)
            num_spheres = struct.unpack('<I', data[offset:offset+4])[0]
            offset += 4
            
            # Spheres
            model.spheres, offset = self._parse_spheres(data, offset, num_spheres, COLVersion.COL_1)
            
            # Unknown data count (4 bytes) - always 0
            num_unknown = struct.unpack('<I', data[offset:offset+4])[0]
            offset += 4
            
            # Number of boxes (4 bytes)
            num_boxes = struct.unpack('<I', data[offset:offset+4])[0]
            offset += 4
            
            # Boxes
            model.boxes, offset = self._parse_boxes(data, offset, num_boxes, COLVersion.COL_1)
            
            # Number of vertices (4 bytes)
            num_vertices = struct.unpack('<I', data[offset:offset+4])[0]
            offset += 4
            
            # Vertices
            model.vertices, offset = self._parse_vertices_col1(data, offset, num_vertices)
            
            # Number of faces (4 bytes)
            num_faces = struct.unpack('<I', data[offset:offset+4])[0]
            offset += 4
            
            # Faces
            model.faces, offset = self._parse_faces_col1(data, offset, num_faces)
            
            return model, offset
            
        except Exception as e:
            self.errors.append(f"COL1 body parse error: {e}")
            return model, offset
    
    def _parse_col23_body(self, data: bytes, model: COLModel) -> COLModel: #vers 1
        """Parse COL2/3 body using offsets from header"""
        try:
            pd = model._parse_data
            base = pd['base_offset']
            
            # Spheres
            if pd['num_spheres'] > 0:
                sphere_offset = base + pd['offset_spheres']
                model.spheres, _ = self._parse_spheres(data, sphere_offset, pd['num_spheres'], model.version)
            
            # Boxes
            if pd['num_boxes'] > 0:
                box_offset = base + pd['offset_boxes']
                model.boxes, _ = self._parse_boxes(data, box_offset, pd['num_boxes'], model.version)
            
            # Vertices - count not stored, calculate from faces
            if pd['num_faces'] > 0:
                vertex_offset = base + pd['offset_vertices']
                # Read all faces first to find max vertex index
                face_offset = base + pd['offset_faces']
                temp_faces, _ = self._parse_faces_col23(data, face_offset, pd['num_faces'])
                
                # Find max vertex index
                max_idx = 0
                for face in temp_faces:
                    max_idx = max(max_idx, face.a, face.b, face.c)
                
                num_vertices = max_idx + 1
                model.vertices, _ = self._parse_vertices_col23(data, vertex_offset, num_vertices)
                model.faces = temp_faces
                
                # Face groups (optional)
                if model.has_face_groups:
                    # Face groups are before faces, work backwards
                    model.face_groups = self._parse_face_groups(data, face_offset)
            
            # Shadow mesh (COL3 only)
            if model.has_shadow_mesh and pd['num_shadow_faces'] > 0:
                shadow_v_offset = base + pd['offset_shadow_vertices']
                shadow_f_offset = base + pd['offset_shadow_faces']
                
                # Parse shadow faces first to get vertex count
                temp_shadow_faces, _ = self._parse_faces_col23(data, shadow_f_offset, pd['num_shadow_faces'])
                
                max_idx = 0
                for face in temp_shadow_faces:
                    max_idx = max(max_idx, face.a, face.b, face.c)
                
                num_shadow_vertices = max_idx + 1
                model.shadow_vertices, _ = self._parse_vertices_col23(data, shadow_v_offset, num_shadow_vertices)
                model.shadow_faces = temp_shadow_faces
            
            # Clean up temporary parse data
            del model._parse_data
            
            return model
            
        except Exception as e:
            self.errors.append(f"COL2/3 body parse error: {e}")
            return model
    
    def _parse_bounding_box_col1(self, data: bytes, offset: int) -> Tuple[BoundingBox, int]: #vers 1
        """Parse COL1 bounding box - 40 bytes
        Structure: radius(4) + center(12) + min(12) + max(12)
        """
        bbox = BoundingBox()
        
        # Radius (4 bytes)
        bbox.radius = struct.unpack('<f', data[offset:offset+4])[0]
        offset += 4
        
        # Center (12 bytes)
        cx, cy, cz = struct.unpack('<fff', data[offset:offset+12])
        bbox.center = Vector3(cx, cy, cz)
        offset += 12
        
        # Min (12 bytes)
        minx, miny, minz = struct.unpack('<fff', data[offset:offset+12])
        bbox.min = Vector3(minx, miny, minz)
        offset += 12
        
        # Max (12 bytes)
        maxx, maxy, maxz = struct.unpack('<fff', data[offset:offset+12])
        bbox.max = Vector3(maxx, maxy, maxz)
        offset += 12
        
        return bbox, offset
    
    def _parse_bounding_box_col23(self, data: bytes, offset: int) -> Tuple[BoundingBox, int]: #vers 1
        """Parse COL2/3 bounding box - 40 bytes
        Structure: min(12) + max(12) + center(12) + radius(4)
        """
        bbox = BoundingBox()
        
        # Min (12 bytes)
        minx, miny, minz = struct.unpack('<fff', data[offset:offset+12])
        bbox.min = Vector3(minx, miny, minz)
        offset += 12
        
        # Max (12 bytes)
        maxx, maxy, maxz = struct.unpack('<fff', data[offset:offset+12])
        bbox.max = Vector3(maxx, maxy, maxz)
        offset += 12
        
        # Center (12 bytes)
        cx, cy, cz = struct.unpack('<fff', data[offset:offset+12])
        bbox.center = Vector3(cx, cy, cz)
        offset += 12
        
        # Radius (4 bytes)
        bbox.radius = struct.unpack('<f', data[offset:offset+4])[0]
        offset += 4
        
        return bbox, offset
    
    def _parse_spheres(self, data: bytes, offset: int, count: int, version: COLVersion) -> Tuple[List[COLSphere], int]: #vers 1
        """Parse collision spheres - 20 bytes each"""
        spheres = []
        
        for i in range(count):
            sphere = COLSphere()
            
            if version == COLVersion.COL_1:
                # COL1: radius + center + surface
                sphere.radius = struct.unpack('<f', data[offset:offset+4])[0]
                offset += 4
                
                cx, cy, cz = struct.unpack('<fff', data[offset:offset+12])
                sphere.center = Vector3(cx, cy, cz)
                offset += 12
            else:
                # COL2/3: center + radius + surface
                cx, cy, cz = struct.unpack('<fff', data[offset:offset+12])
                sphere.center = Vector3(cx, cy, cz)
                offset += 12
                
                sphere.radius = struct.unpack('<f', data[offset:offset+4])[0]
                offset += 4
            
            # Surface (4 bytes)
            sphere.material = struct.unpack('<B', data[offset:offset+1])[0]
            offset += 1
            flags = struct.unpack('<B', data[offset:offset+1])[0]
            offset += 1
            sphere.flags = struct.unpack('<H', data[offset:offset+2])[0]
            offset += 2
            
            spheres.append(sphere)
        
        return spheres, offset
    
    def _parse_boxes(self, data: bytes, offset: int, count: int, version: COLVersion) -> Tuple[List[COLBox], int]: #vers 1
        """Parse collision boxes - 28 bytes each"""
        boxes = []
        
        for i in range(count):
            box = COLBox()
            
            # Min point (12 bytes)
            minx, miny, minz = struct.unpack('<fff', data[offset:offset+12])
            box.min_point = Vector3(minx, miny, minz)
            offset += 12
            
            # Max point (12 bytes)
            maxx, maxy, maxz = struct.unpack('<fff', data[offset:offset+12])
            box.max_point = Vector3(maxx, maxy, maxz)
            offset += 12
            
            # Surface (4 bytes)
            box.material = struct.unpack('<B', data[offset:offset+1])[0]
            offset += 1
            offset += 1  # flags byte
            offset += 2  # padding
            
            if version == COLVersion.COL_1:
                # COL1 has additional flags
                box.flags = struct.unpack('<I', data[offset:offset+4])[0]
                offset += 4
            
            boxes.append(box)
        
        return boxes, offset
    
    def _parse_vertices_col1(self, data: bytes, offset: int, count: int) -> Tuple[List[COLVertex], int]: #vers 1
        """Parse COL1 vertices - 12 bytes each (float[3])"""
        vertices = []
        
        for i in range(count):
            x, y, z = struct.unpack('<fff', data[offset:offset+12])
            vertex = COLVertex(Vector3(x, y, z))
            vertices.append(vertex)
            offset += 12
        
        return vertices, offset
    
    def _parse_vertices_col23(self, data: bytes, offset: int, count: int) -> Tuple[List[COLVertex], int]: #vers 1
        """Parse COL2/3 vertices - 6 bytes each (int16[3])
        CRITICAL: Divide by 128.0 to convert fixed-point to float
        """
        vertices = []
        
        for i in range(count):
            x_int, y_int, z_int = struct.unpack('<hhh', data[offset:offset+6])
            
            # Convert fixed-point to float
            x = float(x_int) / 128.0
            y = float(y_int) / 128.0
            z = float(z_int) / 128.0
            
            vertex = COLVertex(Vector3(x, y, z))
            vertices.append(vertex)
            offset += 6
        
        # Optional 2-byte padding for 4-byte alignment
        if (count * 6) % 4 != 0:
            offset += 2
        
        return vertices, offset
    
    def _parse_faces_col1(self, data: bytes, offset: int, count: int) -> Tuple[List[COLFace], int]: #vers 1
        """Parse COL1 faces - 16 bytes each"""
        faces = []
        
        for i in range(count):
            face = COLFace()
            
            # Vertex indices (3 * 4 = 12 bytes)
            face.a = struct.unpack('<I', data[offset:offset+4])[0]
            offset += 4
            face.b = struct.unpack('<I', data[offset:offset+4])[0]
            offset += 4
            face.c = struct.unpack('<I', data[offset:offset+4])[0]
            offset += 4
            
            # Material (2 bytes)
            face.material = struct.unpack('<H', data[offset:offset+2])[0]
            offset += 2
            
            # Light (2 bytes) - unused in COL1
            offset += 2
            
            faces.append(face)
        
        return faces, offset
    
    def _parse_faces_col23(self, data: bytes, offset: int, count: int) -> Tuple[List[COLFace], int]: #vers 1
        """Parse COL2/3 faces - 8 bytes each"""
        faces = []
        
        for i in range(count):
            face = COLFace()
            
            # Vertex indices (3 * 2 = 6 bytes)
            face.a = struct.unpack('<H', data[offset:offset+2])[0]
            offset += 2
            face.b = struct.unpack('<H', data[offset:offset+2])[0]
            offset += 2
            face.c = struct.unpack('<H', data[offset:offset+2])[0]
            offset += 2
            
            # Material (1 byte)
            face.material = struct.unpack('<B', data[offset:offset+1])[0]
            offset += 1
            
            # Light (1 byte)
            face.light = struct.unpack('<B', data[offset:offset+1])[0]
            offset += 1
            
            faces.append(face)
        
        return faces, offset
    
    def _parse_face_groups(self, data: bytes, face_offset: int) -> List[COLFaceGroup]: #vers 1
        """Parse face groups - work backwards from face array
        Face groups are stored before faces: [groups][count][faces]
        """
        groups = []
        
        try:
            # Read group count (4 bytes before faces)
            count_offset = face_offset - 4
            num_groups = struct.unpack('<I', data[count_offset:count_offset+4])[0]
            
            # Groups are before count (28 bytes each)
            groups_offset = count_offset - (num_groups * 28)
            
            for i in range(num_groups):
                group = COLFaceGroup()
                offset = groups_offset + (i * 28)
                
                # Min (12 bytes)
                minx, miny, minz = struct.unpack('<fff', data[offset:offset+12])
                group.min = Vector3(minx, miny, minz)
                offset += 12
                
                # Max (12 bytes)
                maxx, maxy, maxz = struct.unpack('<fff', data[offset:offset+12])
                group.max = Vector3(maxx, maxy, maxz)
                offset += 12
                
                # Face range (4 bytes)
                group.start_face = struct.unpack('<H', data[offset:offset+2])[0]
                offset += 2
                group.end_face = struct.unpack('<H', data[offset:offset+2])[0]
                offset += 2
                
                groups.append(group)
            
            return groups
            
        except Exception as e:
            self.errors.append(f"Face group parse error: {e}")
            return []


# Convenience function
def parse_col_file(file_path: str, debug: bool = False) -> Tuple[List[COLModel], List[str]]: #vers 1
    """Parse COL file - convenience function
    
    Args:
        file_path: Path to COL file
        debug: Enable debug output
        
    Returns:
        Tuple of (models list, errors list)
    """
    parser = COLParser(debug=debug)
    return parser.parse_col_file(file_path)


# Export
__all__ = ['COLParser', 'parse_col_file']
