#this belongs in methods/col_workshop_loader.py - Version: 1
# X-Seti - December21 2025 - Col Workshop - COL File Loader
"""
COL File Loader - High-level interface for loading COL files
Handles single and multi-model archives
"""

import os
from typing import List, Optional, Tuple
from apps.methods.col_workshop_parser import COLParser
from apps.methods.col_workshop_structures import COLModel, COLVersion

##Classes list -
# COLFile

class COLFile: #vers 1
    """High-level COL file interface"""
    
    def __init__(self, debug: bool = False): #vers 1
        """Initialize COL file handler"""
        self.parser = COLParser(debug=debug)
        self.debug = debug
        self.models: List[COLModel] = []
        self.file_path: Optional[str] = None
        self.raw_data: Optional[bytes] = None
    
    def load(self, file_path: str) -> bool: #vers 1
        """
        Load COL file from disk
        
        Returns: True if successful
        """
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"COL file not found: {file_path}")
            
            # Read file data
            with open(file_path, 'rb') as f:
                self.raw_data = f.read()
            
            self.file_path = file_path
            
            # Parse models
            self.models = self._parse_all_models(self.raw_data)
            
            if self.debug:
                print(f"Loaded {len(self.models)} models from {os.path.basename(file_path)}")
            
            return True
            
        except Exception as e:
            if self.debug:
                print(f"Error loading COL file: {e}")
            return False
    
    def load_from_data(self, data: bytes, name: str = "unknown.col") -> bool: #vers 1
        """
        Load COL from raw bytes
        
        Returns: True if successful
        """
        try:
            self.raw_data = data
            self.file_path = name
            
            # Parse models
            self.models = self._parse_all_models(data)
            
            if self.debug:
                print(f"Loaded {len(self.models)} models from data")
            
            return True
            
        except Exception as e:
            if self.debug:
                print(f"Error loading COL data: {e}")
            return False
    
    def get_model_count(self) -> int: #vers 1
        """Get number of models in file"""
        return len(self.models)
    
    def get_model(self, index: int) -> Optional[COLModel]: #vers 1
        """Get model by index"""
        if 0 <= index < len(self.models):
            return self.models[index]
        return None
    
    def get_model_by_name(self, name: str) -> Optional[COLModel]: #vers 1
        """Get model by name"""
        for model in self.models:
            if model.header.name == name:
                return model
        return None
    
    def get_stats(self) -> dict: #vers 1
        """Get file statistics"""
        total_spheres = sum(len(m.spheres) for m in self.models)
        total_boxes = sum(len(m.boxes) for m in self.models)
        total_vertices = sum(len(m.vertices) for m in self.models)
        total_faces = sum(len(m.faces) for m in self.models)
        
        versions = set(m.header.version for m in self.models)
        
        return {
            'file_path': self.file_path,
            'model_count': len(self.models),
            'versions': [v.name for v in versions],
            'total_spheres': total_spheres,
            'total_boxes': total_boxes,
            'total_vertices': total_vertices,
            'total_faces': total_faces,
            'file_size': len(self.raw_data) if self.raw_data else 0
        }
    
    def is_multi_model(self) -> bool: #vers 1
        """Check if file contains multiple models"""
        return len(self.models) > 1
    
    def _parse_all_models(self, data: bytes) -> List[COLModel]: #vers 1
        """
        Parse all models from data
        COL files have no header - models stored linearly
        """
        models = []
        offset = 0
        
        while offset < len(data):
            try:
                # Check if we have enough data for a header
                if len(data) < offset + 8:
                    break
                
                # Peek at FourCC to validate
                fourcc = data[offset:offset+4]
                if fourcc not in [b'COLL', b'COL2', b'COL3', b'COL4']:
                    if self.debug:
                        print(f"Invalid FourCC at offset {offset}: {fourcc}")
                    break
                
                # Parse model (COL1 only for now)
                if fourcc == b'COLL':
                    model, new_offset = self.parser.parse_col1_model(data, offset)
                    models.append(model)
                    
                    # Move to next model
                    # Size in header is from after size field, so add 8 for fourcc+size
                    model_size = model.header.size + 8
                    offset += model_size
                else:
                    # COL2/3/4 not implemented yet
                    if self.debug:
                        print(f"COL2/3/4 parsing not implemented yet")
                    break
                    
            except Exception as e:
                if self.debug:
                    print(f"Error parsing model at offset {offset}: {e}")
                break
        
        return models
    
    def validate(self) -> Tuple[bool, List[str]]: #vers 1
        """
        Validate COL file
        
        Returns: (is_valid, list_of_errors)
        """
        errors = []
        
        if not self.raw_data:
            errors.append("No data loaded")
            return False, errors
        
        if len(self.models) == 0:
            errors.append("No valid models found")
            return False, errors
        
        # Validate each model
        for i, model in enumerate(self.models):
            # Check for zero-length model name
            if not model.header.name:
                errors.append(f"Model {i}: Empty name")
            
            # Check vertex indices in faces
            num_verts = len(model.vertices)
            for j, face in enumerate(model.faces):
                if face.a >= num_verts or face.b >= num_verts or face.c >= num_verts:
                    errors.append(f"Model {i}, Face {j}: Invalid vertex index")
        
        return len(errors) == 0, errors
