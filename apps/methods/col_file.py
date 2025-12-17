#this belongs in methods/col_file.py - Version: 1
# X-Seti - December17 2025 - Col Workshop - COL File Manager

"""
COL File Manager - High-level interface for loading/saving COL files
Uses col_parser.py for reading and will use col_writer.py for writing
"""

from typing import List, Optional
from pathlib import Path

from apps.methods.col_data_structures import COLModel
from apps.methods.col_parser import COLParser

##Methods list -
# load_from_file
# save_to_file
# add_model
# remove_model
# get_model
# get_model_count

class COLFile: #vers 1
    """COL File - High-level interface for COL file operations"""
    
    def __init__(self, file_path: Optional[str] = None):
        """Initialize COL file
        
        Args:
            file_path: Optional path to COL file to load
        """
        self.file_path = file_path
        self.models: List[COLModel] = []
        self.is_loaded = False
        self.load_error = None
        self.parse_errors = []
    
    def load_from_file(self, file_path: str, debug: bool = False) -> bool: #vers 1
        """Load COL file from disk
        
        Args:
            file_path: Path to COL file
            debug: Enable debug output
            
        Returns:
            True if successful, False otherwise
        """
        try:
            self.file_path = file_path
            self.is_loaded = False
            self.load_error = None
            self.parse_errors = []
            
            # Parse file
            parser = COLParser(debug=debug)
            models, errors = parser.parse_col_file(file_path)
            
            if not models and errors:
                self.load_error = "; ".join(errors)
                self.parse_errors = errors
                return False
            
            self.models = models
            self.parse_errors = errors
            self.is_loaded = True
            
            if debug:
                print(f"[COLFile] Loaded {len(models)} models from {Path(file_path).name}")
                if errors:
                    print(f"[COLFile] Warnings: {len(errors)}")
            
            return True
            
        except Exception as e:
            self.load_error = f"Load failed: {e}"
            return False
    
    def save_to_file(self, file_path: Optional[str] = None) -> bool: #vers 1
        """Save COL file to disk
        
        Args:
            file_path: Optional path to save to (uses self.file_path if None)
            
        Returns:
            True if successful, False otherwise
        """
        # TODO: Implement COL writer
        self.load_error = "COL writer not yet implemented"
        return False
    
    def add_model(self, model: COLModel) -> None: #vers 1
        """Add model to file
        
        Args:
            model: COL model to add
        """
        self.models.append(model)
    
    def remove_model(self, index: int) -> bool: #vers 1
        """Remove model by index
        
        Args:
            index: Model index to remove
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if 0 <= index < len(self.models):
                del self.models[index]
                return True
            return False
        except Exception:
            return False
    
    def get_model(self, index: int) -> Optional[COLModel]: #vers 1
        """Get model by index
        
        Args:
            index: Model index
            
        Returns:
            COL model or None
        """
        try:
            if 0 <= index < len(self.models):
                return self.models[index]
            return None
        except Exception:
            return None
    
    def get_model_count(self) -> int: #vers 1
        """Get number of models in file
        
        Returns:
            Model count
        """
        return len(self.models)
    
    def __repr__(self):
        return f"COLFile(path='{self.file_path}', models={len(self.models)}, loaded={self.is_loaded})"


# Export
__all__ = ['COLFile']
