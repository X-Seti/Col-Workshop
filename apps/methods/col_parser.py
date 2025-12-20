#this belongs in methods/col_parser.py - Version: 1
# X-Seti - December18 2025 - Col Workshop - COL Parser
"""
COL Parser - Comprehensive collision file parser
Handles COL1, COL2, COL3, COL4 format versions
Based on OpenRW implementation with fixed-point vertex conversion
"""

import struct
from typing import Tuple, Optional
from apps.methods.col_data_structures import (
    Vector3, BoundingBox, COLVersion, COLMaterial,
    COLSphere, COLBox, COLVertex, COLFace, COLModel
)
from apps.debug.debug_functions import img_debugger

##Methods list -
# parse_bounds
# parse_boxes
# parse_counts
# parse_faces
# parse_header
# parse_model
# parse_spheres
# parse_vertices

##Classes -
# COLParser

class COLParser:
    """COL file parser for all format versions"""
    
    def __init__(self, debug: bool = True):
        self.debug = debug
    
    def parse_header(self, data: bytes, offset: int = 0) -> Tuple[str, int, str, int, COLVersion, int]: #vers 1
        """Parse COL model header (32 bytes)
        
        Returns: (signature, file_size, model_name, model_id, version, new_offset)
        """
        try:
            if len(data) < offset + 32:
                raise ValueError("Data too short for COL header")
            
            # Signature (4 bytes)
            signature = data[offset:offset+4].decode('ascii', errors='ignore')
            offset += 4
            
            # File size (4 bytes)
            file_size = struct.unpack('<I', data[offset:offset+4])[0]
            offset += 4
            
            # Model name (22 bytes, null-terminated)
            name_bytes = data[offset:offset+22]
            model_name = name_bytes.split(b'\x00')[0].decode('ascii', errors='ignore')
            offset += 22
            
            # Model ID (2 bytes)
            model_id = struct.unpack('<H', data[offset:offset+2])[0]
            offset += 2
            
            # Determine version
            version = COLVersion.COL_1
            if signature.startswith('COL'):
                version_char = signature[3] if len(signature) > 3 else '1'
                if version_char == '\x02':
                    version = COLVersion.COL_2
                elif version_char == '\x03':
                    version = COLVersion.COL_3
                elif version_char == '\x04':
                    version = COLVersion.COL_4
            
            if self.debug:
                img_debugger.debug(f"Header: {signature} v{version.value}, '{model_name}', ID:{model_id}")
            
            return signature, file_size, model_name, model_id, version, offset
            
        except Exception as e:
            raise ValueError(f"Header parse error: {str(e)}")
    

    def parse_bounds(self, data: bytes, offset: int, version: COLVersion) -> Tuple[BoundingBox, int]: #vers 1
        """Parse bounding box (40 bytes for COL1, 28 bytes for COL2/3)
        
        Returns: (bounding_box, new_offset)
        """
        try:
            bbox = BoundingBox()
            
            if version == COLVersion.COL_1:
                # COL1: radius + center + min + max (40 bytes)
                if len(data) < offset + 40:
                    raise ValueError("Data too short for COL1 bounds")
                
                bbox.radius = struct.unpack('<f', data[offset:offset+4])[0]
                offset += 4
                
                cx, cy, cz = struct.unpack('<fff', data[offset:offset+12])
                bbox.center = Vector3(cx, cy, cz)
                offset += 12
                
                min_x, min_y, min_z = struct.unpack('<fff', data[offset:offset+12])
                bbox.min = Vector3(min_x, min_y, min_z)
                offset += 12
                
                max_x, max_y, max_z = struct.unpack('<fff', data[offset:offset+12])
                bbox.max = Vector3(max_x, max_y, max_z)
                offset += 12
            else:
                # COL2/3: min + max + center + radius (28 bytes)
                if len(data) < offset + 28:
                    raise ValueError("Data too short for COL2/3 bounds")
                
                min_x, min_y, min_z = struct.unpack('<fff', data[offset:offset+12])
                bbox.min = Vector3(min_x, min_y, min_z)
                offset += 12
                
                max_x, max_y, max_z = struct.unpack('<fff', data[offset:offset+12])
                bbox.max = Vector3(max_x, max_y, max_z)
                offset += 12
                
                cx, cy, cz = struct.unpack('<fff', data[offset:offset+12])
                bbox.center = Vector3(cx, cy, cz)
                offset += 12
                
                bbox.radius = struct.unpack('<f', data[offset:offset+4])[0]
                offset += 4
            
            if self.debug:
                img_debugger.debug(f"Bounds: r={bbox.radius:.2f}, center={bbox.center}")
            
            return bbox, offset
            
        except Exception as e:
            raise ValueError(f"Bounds parse error: {str(e)}")
    

    def parse_counts(self, data: bytes, offset: int, version: COLVersion) -> Tuple[int, int, int, int, int]: #vers 1
        """Parse collision element counts
        
        Returns: (num_spheres, num_boxes, num_vertices, num_faces, new_offset)
        """
        try:
            if version == COLVersion.COL_1:
                # COL1: spheres, unknown, boxes, vertices, faces (20 bytes)
                if len(data) < offset + 20:
                    raise ValueError("Data too short for COL1 counts")
                
                num_spheres = struct.unpack('<I', data[offset:offset+4])[0]
                offset += 4
                num_unknown = struct.unpack('<I', data[offset:offset+4])[0]
                offset += 4
                num_boxes = struct.unpack('<I', data[offset:offset+4])[0]
                offset += 4
                num_vertices = struct.unpack('<I', data[offset:offset+4])[0]
                offset += 4
                num_faces = struct.unpack('<I', data[offset:offset+4])[0]
                num_spheres = struct.unpack('<I', data[offset:offset+4])[0]
                offset += 4
                num_boxes = struct.unpack('<I', data[offset:offset+4])[0]
                offset += 4
                num_faces = struct.unpack('<I', data[offset:offset+4])[0]
                offset += 4
                num_vertices = struct.unpack('<I', data[offset:offset+4])[0]
                offset += 4
            
            if self.debug:
                img_debugger.debug(f"Counts: S:{num_spheres} B:{num_boxes} V:{num_vertices} F:{num_faces}")
            
            return num_spheres, num_boxes, num_vertices, num_faces, offset
            
        except Exception as e:
            raise ValueError(f"Counts parse error: {str(e)}")
    

    def parse_spheres(self, data: bytes, offset: int, count: int, version: COLVersion) -> Tuple[list, int]: #vers 1
        """Parse collision spheres
        
        COL1: 24 bytes each (center + radius + material + flags)
        COL2/3: 20 bytes each (center + radius + material)
        
        Returns: (spheres_list, new_offset)
        """
        try:
            spheres = []
            sphere_size = 24 if version == COLVersion.COL_1 else 20
            
            if len(data) < offset + (count * sphere_size):
                raise ValueError(f"Data too short for {count} spheres")
            
            for i in range(count):
                # Center (12 bytes)
                cx, cy, cz = struct.unpack('<fff', data[offset:offset+12])
                center = Vector3(cx, cy, cz)
                offset += 12
                
                # Radius (4 bytes)
                radius = struct.unpack('<f', data[offset:offset+4])[0]
                offset += 4
                
                # Material (4 bytes)
                material_id = struct.unpack('<I', data[offset:offset+4])[0]
                offset += 4
                
                # Flags (COL1 only, 4 bytes)
                flags = 0
                if version == COLVersion.COL_1:
                    flags = struct.unpack('<I', data[offset:offset+4])[0]
                    offset += 4
                
                material = COLMaterial(material_id, flags)
                sphere = COLSphere(center, radius, material)
                spheres.append(sphere)
            
            if self.debug:
                img_debugger.debug(f"Parsed {len(spheres)} spheres")
            
            return spheres, offset
            
        except Exception as e:
            raise ValueError(f"Spheres parse error: {str(e)}")
    

    def parse_boxes(self, data: bytes, offset: int, count: int, version: COLVersion) -> Tuple[list, int]: #vers 1
        """Parse collision boxes
        
        COL1: 32 bytes each (min + max + material + flags)
        COL2/3: 28 bytes each (min + max + material)
        
        Returns: (boxes_list, new_offset)
        """
        try:
            boxes = []
            box_size = 32 if version == COLVersion.COL_1 else 28
            
            if len(data) < offset + (count * box_size):
                raise ValueError(f"Data too short for {count} boxes")
            
            for i in range(count):
                # Min point (12 bytes)
                min_x, min_y, min_z = struct.unpack('<fff', data[offset:offset+12])
                min_point = Vector3(min_x, min_y, min_z)
                offset += 12
                
                # Max point (12 bytes)
                max_x, max_y, max_z = struct.unpack('<fff', data[offset:offset+12])
                max_point = Vector3(max_x, max_y, max_z)
                offset += 12
                
                # Material (4 bytes)
                material_id = struct.unpack('<I', data[offset:offset+4])[0]
                offset += 4
                
                # Flags (COL1 only, 4 bytes)
                flags = 0
                if version == COLVersion.COL_1:
                    flags = struct.unpack('<I', data[offset:offset+4])[0]
                    offset += 4
                
                material = COLMaterial(material_id, flags)
                box = COLBox(min_point, max_point, material)
                boxes.append(box)
            
            if self.debug:
                img_debugger.debug(f"Parsed {len(boxes)} boxes")
            
            return boxes, offset
            
        except Exception as e:
            raise ValueError(f"Boxes parse error: {str(e)}")
    

    def parse_vertices(self, data: bytes, offset: int, count: int, version: COLVersion) -> Tuple[list, int]: #vers 1
        """Parse mesh vertices
        
        COL1: 12 bytes each (3 floats)
        COL2/3: 6 bytes each (3 int16, CRITICAL: divide by 128.0 for fixed-point conversion)
        
        Returns: (vertices_list, new_offset)
        """
        try:
            vertices = []
            
            if version == COLVersion.COL_1:
                # COL1: float vertices (12 bytes each)
                vertex_size = 12
                if len(data) < offset + (count * vertex_size):
                    raise ValueError(f"Data too short for {count} COL1 vertices")
                
                for i in range(count):
                    x, y, z = struct.unpack('<fff', data[offset:offset+12])
                    position = Vector3(x, y, z)
                    offset += 12
                    vertices.append(COLVertex(position))
            else:
                # COL2/3: int16 vertices (6 bytes each) - CRITICAL FIX: divide by 128.0
                vertex_size = 6
                if len(data) < offset + (count * vertex_size):
                    raise ValueError(f"Data too short for {count} COL2/3 vertices")
                
                for i in range(count):
                    x_int, y_int, z_int = struct.unpack('<hhh', data[offset:offset+6])
                    # CRITICAL: Convert int16 fixed-point to float
                    x = x_int / 128.0
                    y = y_int / 128.0
                    z = z_int / 128.0
                    position = Vector3(x, y, z)
                    offset += 6
                    vertices.append(COLVertex(position))
            
            if self.debug:
                img_debugger.debug(f"Parsed {len(vertices)} vertices")
            
            return vertices, offset
            
        except Exception as e:
            raise ValueError(f"Vertices parse error: {str(e)}")


    def parse_faces(self, data: bytes, offset: int, count: int, version: COLVersion) -> Tuple[list, int]: #vers 1
        """Parse mesh faces
        
        COL1: 16 bytes each (indices + material + light + flags)
        COL2/3: 12 bytes each (indices + material + light + padding)
        
        Returns: (faces_list, new_offset)
        """
        try:
            faces = []
            face_size = 16 if version == COLVersion.COL_1 else 12
            
            if len(data) < offset + (count * face_size):
                raise ValueError(f"Data too short for {count} faces")
            
            for i in range(count):
                # Vertex indices (6 bytes - 3 uint16)
                a, b, c = struct.unpack('<HHH', data[offset:offset+6])
                vertex_indices = (a, b, c)
                offset += 6
                
                # Material (2 bytes)
                material_id = struct.unpack('<H', data[offset:offset+2])[0]
                offset += 2
                
                # Light (2 bytes)
                light = struct.unpack('<H', data[offset:offset+2])[0]
                offset += 2
                
                if version == COLVersion.COL_1:
                    # Flags (4 bytes)
                    flags = struct.unpack('<I', data[offset:offset+4])[0]
                    offset += 4
                    material = COLMaterial(material_id, flags)
                else:
                    # Padding (2 bytes)
                    offset += 2
                    material = COLMaterial(material_id, 0)
                
                face = COLFace(vertex_indices, material, light)
                faces.append(face)
            
            if self.debug:
                img_debugger.debug(f"Parsed {len(faces)} faces")
            
            return faces, offset
            
        except Exception as e:
            raise ValueError(f"Faces parse error: {str(e)}")
    

    def parse_model(self, data: bytes, offset: int = 0) -> Tuple[Optional[COLModel], int]: #vers 1
        """Parse complete COL model
        
        Returns: (model, new_offset) or (None, offset) on error
        """
        try:
            model = COLModel()
            start_offset = offset
            
            # Parse header (32 bytes)
            signature, file_size, model_name, model_id, version, offset = self.parse_header(data, offset)
            model.name = model_name
            model.model_id = model_id
            model.version = version
            
            # Parse bounds
            model.bounding_box, offset = self.parse_bounds(data, offset, version)
            
            # Parse counts
            num_spheres, num_boxes, num_vertices, num_faces, offset = self.parse_counts(data, offset, version)
            
            # Sanity check counts
            if num_vertices > 100000 or num_faces > 100000:
                if self.debug:
                    img_debugger.warning(f"Skipping model with unrealistic counts: V:{num_vertices} F:{num_faces}")
                return None, offset
            
            # Parse collision elements
            model.spheres, offset = self.parse_spheres(data, offset, num_spheres, version)
            model.boxes, offset = self.parse_boxes(data, offset, num_boxes, version)
            model.vertices, offset = self.parse_vertices(data, offset, num_vertices, version)
            
            
            model.faces, offset = self.parse_faces(data, offset, num_faces, version)
            
            # Update flags
            model.update_flags()
            
            bytes_read = offset - start_offset
            if self.debug:
                img_debugger.success(f"Model parsed: {bytes_read} bytes, {model.get_stats()}")
            
            return model, offset
            
        except Exception as e:
            if self.debug:
                import traceback
            img_debugger.error(f"Model parse failed: {str(e)}")
            img_debugger.error(traceback.format_exc())
            return None, offset


# Export parser
__all__ = ['COLParser']
