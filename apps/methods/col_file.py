#this belongs in methods/col_file.py - Version: 1
# X-Seti - December18 2025 - Col Workshop - COL File
"""
COL File - High-level interface for collision files
Handles loading, multi-model detection, and file management
"""

import os
from typing import List, Optional
from apps.methods.col_data_structures import COLModel
from apps.methods.col_parser import COLParser
from apps.debug.debug_functions import img_debugger

##Methods list -
# get_info
# get_model
# is_multi_model_archive
# load_from_file

##Classes -
# COLFile

class COLFile:
    """COL file container with loading and management"""
    
    def __init__(self, debug: bool = True):
        self.file_path = ""
        self.models: List[COLModel] = []
        self.is_loaded = False
        self.load_error = ""
        self.debug = debug
        self.parser = COLParser(debug=debug)
    
    def load_from_file(self, file_path: str) -> bool: #vers 1
        """Load COL file from disk
        
        Args:
            file_path: Path to COL file
            
        Returns:
            True if successful, False otherwise
        """
        try:
            self.file_path = file_path
            self.models = []
            self.is_loaded = False
            self.load_error = ""
            
            # Validate file
            if not os.path.exists(file_path):
                self.load_error = f"File not found: {file_path}"
                img_debugger.error(self.load_error)
                return False
            
            # Read file data
            with open(file_path, 'rb') as f:
                data = f.read()
            
            file_size = len(data)
            if file_size < 8:
                self.load_error = "File too small to be valid COL"
                img_debugger.error(self.load_error)
                return False
            
            if self.debug:
                img_debugger.info(f"Loading: {os.path.basename(file_path)} ({file_size} bytes)")
            
            # Check for multi-model archive
            if self.is_multi_model_archive(data):
                return self._load_multi_model_archive(data)
            else:
                return self._load_single_model(data)
            
        except Exception as e:
            self.load_error = f"Load error: {str(e)}"
            img_debugger.error(self.load_error)
            return False
    
    def is_multi_model_archive(self, data: bytes) -> bool: #vers 1
        """Check if file contains multiple COL models
        
        Multi-model archives have multiple COL signatures in the file
        
        Args:
            data: File data bytes
            
        Returns:
            True if multi-model archive
        """
        try:
            signature_count = 0
            offset = 0
            
            # Scan for COL signatures
            while offset < len(data) - 4:
                sig = data[offset:offset+4]
                if sig in [b'COLL', b'COL\x02', b'COL\x03', b'COL\x04']:
                    signature_count += 1
                    if signature_count > 1:
                        if self.debug:
                            img_debugger.debug(f"Multi-model archive detected ({signature_count} signatures)")
                        return True
                    # Skip ahead to avoid counting same signature
                    offset += 100
                else:
                    offset += 1
            
            return False
            
        except Exception:
            return False
    
    def _load_single_model(self, data: bytes) -> bool: #vers 1
        """Load single COL model
        
        Args:
            data: File data bytes
            
        Returns:
            True if successful
        """
        try:
            model, offset = self.parser.parse_model(data, 0)
            
            if model is None:
                self.load_error = "Failed to parse COL model"
                return False
            
            self.models.append(model)
            self.is_loaded = True
            
            if self.debug:
                img_debugger.success(f"Loaded 1 model: {model.name}")
            
            return True
            
        except Exception as e:
            self.load_error = f"Single model parse error: {str(e)}"
            img_debugger.error(self.load_error)
            return False
    
    def _load_multi_model_archive(self, data: bytes) -> bool: #vers 1
        """Load multi-model COL archive
        
        Archives contain multiple independent COL models,
        each starting with its own signature
        
        Args:
            data: File data bytes
            
        Returns:
            True if at least one model loaded
        """
        try:
            if self.debug:
                img_debugger.info("Parsing multi-model archive...")
            
            # Find all signature positions
            signatures = []
            offset = 0
            
            while offset < len(data) - 4:
                sig = data[offset:offset+4]
                if sig in [b'COLL', b'COL\x02', b'COL\x03', b'COL\x04']:
                    signatures.append(offset)
                    if self.debug:
                        img_debugger.debug(f"Found signature at offset {offset}")
                offset += 1
            
            if not signatures:
                self.load_error = "No COL signatures found"
                return False
            
            # Parse each model
            models_loaded = 0
            for i, sig_offset in enumerate(signatures):
                try:
                    model, new_offset = self.parser.parse_model(data, sig_offset)
                    
                    if model:
                        self.models.append(model)
                        models_loaded += 1
                        if self.debug:
                            img_debugger.debug(f"Archive model {i}: {model.name} loaded")
                    else:
                        if self.debug:
                            img_debugger.warning(f"Archive model {i}: parse failed")
                
                except Exception as e:
                    if self.debug:
                        img_debugger.warning(f"Archive model {i} error: {str(e)}")
                    continue
            
            if models_loaded > 0:
                self.is_loaded = True
                if self.debug:
                    img_debugger.success(f"Archive loaded: {models_loaded} models")
                return True
            else:
                self.load_error = "No models could be loaded from archive"
                return False
            
        except Exception as e:
            self.load_error = f"Archive parse error: {str(e)}"
            img_debugger.error(self.load_error)
            return False
    
    def get_model(self, index: int) -> Optional[COLModel]: #vers 1
        """Get model by index
        
        Args:
            index: Model index (0-based)
            
        Returns:
            COLModel or None if index invalid
        """
        if 0 <= index < len(self.models):
            return self.models[index]
        return None
    
    def get_info(self) -> str: #vers 1
        """Get file information summary
        
        Returns:
            Multi-line string with file details
        """
        lines = []
        
        filename = os.path.basename(self.file_path) if self.file_path else "Unknown"
        lines.append(f"COL File: {filename}")
        lines.append(f"Models: {len(self.models)}")
        lines.append("")
        
        for i, model in enumerate(self.models):
            lines.append(f"Model {i}: {model.name}")
            lines.append(f"  Version: {model.version.name}")
            lines.append(f"  ID: {model.model_id}")
            lines.append(f"  Spheres: {len(model.spheres)}")
            lines.append(f"  Boxes: {len(model.boxes)}")
            lines.append(f"  Vertices: {len(model.vertices)}")
            lines.append(f"  Faces: {len(model.faces)}")
            lines.append("")
        
        return "\n".join(lines)


# Export COLFile
__all__ = ['COLFile']
