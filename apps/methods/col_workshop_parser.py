#this belongs in methods/col_workshop_parser.py - Version: 1
# X-Seti - December21 2025 - Col Workshop - COL Binary Parser
"""
COL Binary Parser - Handles parsing binary COL data
Supports COL1 (GTA3/VC) initially, COL2/3 (SA) to be added
Based on GTA Wiki specification
"""

import struct
from typing import Tuple, List, Optional
from apps.methods.col_workshop_structures import (
    COLHeader, COLBounds, COLSphere, COLBox, 
    COLVertex, COLFace, COLModel, COLVersion
)

##Classes list -
# COLParser

class COLParser: #vers 1
    """Binary parser for COL files"""
    
    def __init__(self, debug: bool = False): #vers 1
        """Initialize parser"""
        self.debug = debug
        
    def parse_header(self, data: bytes, offset: int = 0) -> Tuple[COLHeader, int]: #vers 1
        """
        Parse COL header - 32 bytes total
        
        Returns: (COLHeader, new_offset)
        """
        if len(data) < offset + 32:
            raise ValueError("Data too short for COL header")
        
        # Read FourCC (4 bytes)
        fourcc = data[offset:offset+4]
        offset += 4
        
        # Read size (4 bytes)
        size = struct.unpack('<I', data[offset:offset+4])[0]
        offset += 4
        
        # Read name (22 bytes, null-terminated)
        name_bytes = data[offset:offset+22]
        name = name_bytes.split(b'\x00')[0].decode('ascii', errors='ignore')
        offset += 22
        
        # Read model ID (2 bytes)
        model_id = struct.unpack('<H', data[offset:offset+2])[0]
        offset += 2
        
        # Determine version from fourcc
        version = self._fourcc_to_version(fourcc)
        
        header = COLHeader(
            fourcc=fourcc,
            size=size,
            name=name,
            model_id=model_id,
            version=version
        )
        
        if self.debug:
            print(f"Header: {fourcc} v{version.value}, '{name}', size={size}")
        
        return header, offset
    
    def parse_bounds(self, data: bytes, offset: int, version: COLVersion) -> Tuple[COLBounds, int]: #vers 1
        """
        Parse COL bounds - 40 bytes
        COL1: radius, center, min, max
        COL2/3: min, max, center, radius (reordered)
        """
        if len(data) < offset + 40:
            raise ValueError("Data too short for bounds")
        
        if version == COLVersion.COL_1:
            # COL1 order: radius, center, min, max
            radius = struct.unpack('<f', data[offset:offset+4])[0]
            offset += 4
            
            center = struct.unpack('<fff', data[offset:offset+12])
            offset += 12
            
            min_pt = struct.unpack('<fff', data[offset:offset+12])
            offset += 12
            
            max_pt = struct.unpack('<fff', data[offset:offset+12])
            offset += 12
        else:
            # COL2/3 order: min, max, center, radius
            min_pt = struct.unpack('<fff', data[offset:offset+12])
            offset += 12
            
            max_pt = struct.unpack('<fff', data[offset:offset+12])
            offset += 12
            
            center = struct.unpack('<fff', data[offset:offset+12])
            offset += 12
            
            radius = struct.unpack('<f', data[offset:offset+4])[0]
            offset += 4
        
        bounds = COLBounds(
            radius=radius,
            center=center,
            min=min_pt,
            max=max_pt
        )
        
        return bounds, offset
    
    def parse_spheres(self, data: bytes, offset: int, count: int) -> Tuple[List[COLSphere], int]: #vers 1
        """Parse collision spheres - 20 bytes each (COL1)"""
        spheres = []
        
        for _ in range(count):
            if len(data) < offset + 20:
                raise ValueError("Data too short for sphere")
            
            # Radius (4 bytes)
            radius = struct.unpack('<f', data[offset:offset+4])[0]
            offset += 4
            
            # Center (12 bytes)
            center = struct.unpack('<fff', data[offset:offset+12])
            offset += 12
            
            # Parse spheres
            num_spheres = struct.unpack('<I', data[offset:offset+4])[0]
            offset += 4
            spheres, offset = self.parse_spheres(data, offset, num_spheres)

            # Skip unknown (always 0)
            offset += 4

            # Parse boxes
            num_boxes = struct.unpack('<I', data[offset:offset+4])[0]
            offset += 4
            boxes, offset = self.parse_boxes(data, offset, num_boxes)

            # Parse vertices
            num_vertices = struct.unpack('<I', data[offset:offset+4])[0]
            offset += 4
            vertices, offset = self.parse_vertices(data, offset, num_vertices, header.version)

            # Parse faces
            num_faces = struct.unpack('<I', data[offset:offset+4])[0]
            offset += 4
            faces, offset = self.parse_faces(data, offset, num_faces, header.version)

            # Surface properties (4 bytes)
            material = data[offset]
            flag = data[offset + 1]
            brightness = data[offset + 2]
            light = data[offset + 3]
            offset += 4
            
            sphere = COLSphere(
                radius=radius,
                center=center,
                material=material,
                flag=flag,
                brightness=brightness,
                light=light
            )
            spheres.append(sphere)
        
        return spheres, offset
    
    def parse_boxes(self, data: bytes, offset: int, count: int) -> Tuple[List[COLBox], int]: #vers 1
        """Parse collision boxes - 28 bytes each"""
        boxes = []
        
        for _ in range(count):
            if len(data) < offset + 28:
                raise ValueError("Data too short for box")
            
            # Min point (12 bytes)
            min_pt = struct.unpack('<fff', data[offset:offset+12])
            offset += 12
            
            # Max point (12 bytes)
            max_pt = struct.unpack('<fff', data[offset:offset+12])
            offset += 12
            
            # Surface properties (4 bytes)
            material = data[offset]
            flag = data[offset + 1]
            brightness = data[offset + 2]
            light = data[offset + 3]
            offset += 4
            
            box = COLBox(
                min=min_pt,
                max=max_pt,
                material=material,
                flag=flag,
                brightness=brightness,
                light=light
            )
            boxes.append(box)
        
        return boxes, offset
    
    def parse_vertices(self, data: bytes, offset: int, count: int, version: COLVersion) -> Tuple[List[COLVertex], int]: #vers 1
        """
        Parse mesh vertices
        COL1: 12 bytes each (3 floats)
        COL2/3: 6 bytes each (3 int16 - fixed point)
        """
        vertices = []
        
        if version == COLVersion.COL_1:
            # COL1: float vertices
            for _ in range(count):
                if len(data) < offset + 12:
                    raise ValueError("Data too short for vertex")
                
                x, y, z = struct.unpack('<fff', data[offset:offset+12])
                offset += 12
                
                vertices.append(COLVertex(x=x, y=y, z=z))
        else:
            # COL2/3: int16 fixed-point vertices (divide by 128.0)
            for _ in range(count):
                if len(data) < offset + 6:
                    raise ValueError("Data too short for vertex")
                
                ix, iy, iz = struct.unpack('<hhh', data[offset:offset+6])
                offset += 6
                
                # Convert fixed-point to float
                x = ix / 128.0
                y = iy / 128.0
                z = iz / 128.0
                
                vertices.append(COLVertex(x=x, y=y, z=z))
        
        return vertices, offset
    
    def parse_faces(self, data: bytes, offset: int, count: int, version: COLVersion) -> Tuple[List[COLFace], int]: #vers 1
        """
        Parse mesh faces
        COL1: 16 bytes each (3 uint32 + 4 bytes surface)
        COL2/3: 8 bytes each (3 uint16 + 2 bytes material/light)
        """
        faces = []
        
        if version == COLVersion.COL_1:
            # COL1: uint32 indices
            for _ in range(count):
                if len(data) < offset + 16:
                    raise ValueError("Data too short for face")
                
                # Vertex indices (12 bytes)
                a, b, c = struct.unpack('<III', data[offset:offset+12])
                offset += 12
                
                # Surface properties (4 bytes)
                material = data[offset]
                flag = data[offset + 1]
                brightness = data[offset + 2]
                light = data[offset + 3]
                offset += 4
                
                face = COLFace(
                    a=a, b=b, c=c,
                    material=material,
                    flag=flag,
                    brightness=brightness,
                    light=light
                )
                faces.append(face)
        else:
            # COL2/3: uint16 indices
            for _ in range(count):
                if len(data) < offset + 8:
                    raise ValueError("Data too short for face")
                
                # Vertex indices (6 bytes)
                a, b, c = struct.unpack('<HHH', data[offset:offset+6])
                offset += 6
                
                # Material and light (2 bytes)
                material = data[offset]
                light = data[offset + 1]
                offset += 2
                
                face = COLFace(
                    a=a, b=b, c=c,
                    material=material,
                    flag=0,
                    brightness=0,
                    light=light
                )
                faces.append(face)
        
        return faces, offset
    
    def parse_col1_model(self, data: bytes, offset: int = 0) -> Tuple[COLModel, int]: #vers 1
        """Parse complete COL1 model"""
        start_offset = offset
        
        # Parse header
        header, offset = self.parse_header(data, offset)
        
        if header.version != COLVersion.COL_1:
            raise ValueError(f"Expected COL1, got {header.version}")
        
        # Parse bounds
        bounds, offset = self.parse_bounds(data, offset, header.version)
        
        # Read counts (COL1 format)
        if len(data) < offset + 20:
            raise ValueError("Data too short for COL1 counts")
        
        num_spheres = struct.unpack('<I', data[offset:offset+4])[0]
        offset += 4
        
        num_unknown = struct.unpack('<I', data[offset:offset+4])[0]  # Always 0
        offset += 4
        
        num_boxes = struct.unpack('<I', data[offset:offset+4])[0]
        offset += 4
        
        num_vertices = struct.unpack('<I', data[offset:offset+4])[0]
        offset += 4
        
        num_faces = struct.unpack('<I', data[offset:offset+4])[0]
        offset += 4
        
        if self.debug:
            print(f"COL1 Counts: S={num_spheres} B={num_boxes} V={num_vertices} F={num_faces}")
        
        # Parse spheres
        spheres, offset = self.parse_spheres(data, offset, num_spheres)
        
        # Parse boxes
        boxes, offset = self.parse_boxes(data, offset, num_boxes)
        
        # Parse vertices
        vertices, offset = self.parse_vertices(data, offset, num_vertices, header.version)
        
        # Parse faces
        faces, offset = self.parse_faces(data, offset, num_faces, header.version)
        
        model = COLModel(
            header=header,
            bounds=bounds,
            spheres=spheres,
            boxes=boxes,
            vertices=vertices,
            faces=faces
        )
        
        return model, offset
    
    def _fourcc_to_version(self, fourcc: bytes) -> COLVersion: #vers 1
        """Convert FourCC to version enum"""
        if fourcc == b'COLL':
            return COLVersion.COL_1
        elif fourcc == b'COL2':
            return COLVersion.COL_2
        elif fourcc == b'COL3':
            return COLVersion.COL_3
        elif fourcc == b'COL4':
            return COLVersion.COL_4
        else:
            raise ValueError(f"Unknown COL FourCC: {fourcc}")
