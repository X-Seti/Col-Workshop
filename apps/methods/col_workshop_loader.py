#this belongs in methods/col_workshop_loader.py - Version: 1
# X-Seti - December18 2025 - Col Workshop - File Loader
"""
COL Workshop Loader - Load COL files with progress and error handling
"""

import os
from PyQt6.QtWidgets import QApplication
from apps.methods.col_file import COLFile
from apps.methods.col_parser import COLParser
from apps.gui.col_workshop_dialogs import COLLoadProgressDialog, COLLoadErrorDialog
from apps.debug.debug_functions import img_debugger

##Methods list -
# load_col_with_progress

def load_col_with_progress(file_path: str, parent=None) -> COLFile: #vers 1
    """Load COL file with progress dialog and error handling
    
    Args:
        file_path: Path to COL file
        parent: Parent widget for dialogs
        
    Returns:
        COLFile object or None if aborted
    """
    try:
        # Create progress dialog
        progress = COLLoadProgressDialog(parent)
        progress.set_file_name(os.path.basename(file_path))
        progress.show()
        QApplication.processEvents()
        
        # Read file data
        progress.set_status("Reading file...")
        progress.set_progress(10)
        QApplication.processEvents()
        
        with open(file_path, 'rb') as f:
            data = f.read()
        
        file_size = len(data)
        if file_size < 8:
            img_debugger.error("File too small")
            progress.close()
            return None
        
        # Create COL file object
        col_file = COLFile(debug=False)
        col_file.file_path = file_path
        
        # Check for multi-model archive
        progress.set_status("Detecting format...")
        progress.set_progress(20)
        QApplication.processEvents()
        
        is_archive = col_file.is_multi_model_archive(data)
        
        if is_archive:
            # Parse archive with error handling
            result = _load_archive_with_dialogs(col_file, data, progress, parent)
            progress.close()
            return result if result else None
        else:
            # Parse single model
            progress.set_status("Parsing model...")
            progress.set_progress(50)
            QApplication.processEvents()
            
            parser = COLParser(debug=False)
            model, offset = parser.parse_model(data, 0)
            
            if model:
                col_file.models.append(model)
                col_file.is_loaded = True
                progress.set_model_count(1)
                progress.set_progress(100)
                QApplication.processEvents()
                progress.close()
                return col_file
            else:
                img_debugger.error("Failed to parse single model")
                progress.close()
                return None
        
    except Exception as e:
        img_debugger.error(f"Load error: {str(e)}")
        if 'progress' in locals():
            progress.close()
        return None


def _load_archive_with_dialogs(col_file: COLFile, data: bytes, progress: COLLoadProgressDialog, parent) -> COLFile: #vers 1
    """Load multi-model archive with error dialogs
    
    Args:
        col_file: COLFile object to populate
        data: File data bytes
        progress: Progress dialog
        parent: Parent widget
        
    Returns:
        COLFile object or None if aborted
    """
    try:
        progress.set_status("Scanning for models...")
        QApplication.processEvents()
        
        # Find all signatures
        signatures = []
        offset = 0
        
        while offset < len(data) - 4:
            sig = data[offset:offset+4]
            if sig in [b'COLL', b'COL\x02', b'COL\x03', b'COL\x04']:
                signatures.append(offset)
            offset += 1
        
        if not signatures:
            img_debugger.error("No COL signatures found")
            return None
        
        total = len(signatures)
        progress.set_status(f"Found {total} models, parsing...")
        QApplication.processEvents()
        
        # Parse models
        parser = COLParser(debug=False)
        skip_all_errors = False
        ignore_all_errors = False
        
        for i, sig_offset in enumerate(signatures):
            # Update progress
            pct = 20 + int((i / total) * 70)
            progress.set_progress(pct)
            progress.set_status(f"Parsing model {i+1}/{total}...")
            QApplication.processEvents()
            
            # Check for cancel
            if not progress.isVisible():
                img_debugger.info("Load cancelled by user")
                return None
            
            # Try to get model name first
            model_name = f"Model at offset {sig_offset}"
            try:
                # Peek at header to get name
                if sig_offset + 32 <= len(data):
                    name_bytes = data[sig_offset+8:sig_offset+30]
                    model_name = name_bytes.split(b'\x00')[0].decode('ascii', 'ignore')
                    if not model_name:
                        model_name = f"Model_{i}"
            except:
                pass
            
            try:
                model, new_offset = parser.parse_model(data, sig_offset)
                
                if model:
                    col_file.models.append(model)
                    progress.set_model_count(len(col_file.models))
                    progress.add_model(f"{model.name} (v{model.version.value})")
                    QApplication.processEvents()
                else:
                    # Parse failed - show error dialog unless skip_all or ignore_all
                    if not skip_all_errors and not ignore_all_errors:
                        remaining = total - i - 1
                        error_dialog = COLLoadErrorDialog(
                            model_name,
                            "Failed to parse model structure",
                            remaining,
                            parent
                        )
                        error_dialog.exec()
                        
                        action = error_dialog.get_action()
                        
                        if action == COLLoadErrorDialog.ABORT:
                            img_debugger.info("Load aborted by user")
                            return None
                        elif action == COLLoadErrorDialog.SKIP_ALL:
                            skip_all_errors = True
                            img_debugger.info("Skipping all errors")
                            progress.add_warning(f"Skipped: {model_name} (failed to parse)")
                        elif action == COLLoadErrorDialog.IGNORE_ALL:
                            ignore_all_errors = True
                            img_debugger.info("Ignoring all errors")
                        elif action == COLLoadErrorDialog.SKIP:
                            progress.add_warning(f"Skipped: {model_name} (failed to parse)")
                        # IGNORE: just continue
                    elif skip_all_errors:
                        progress.add_warning(f"Skipped: {model_name} (failed to parse)")
                    # ignore_all: just continue silently
            
            except Exception as e:
                # Parse exception - show error dialog unless skip_all or ignore_all
                if not skip_all_errors and not ignore_all_errors:
                    remaining = total - i - 1
                    error_dialog = COLLoadErrorDialog(
                        model_name,
                        str(e),
                        remaining,
                        parent
                    )
                    error_dialog.exec()
                    
                    action = error_dialog.get_action()
                    
                    if action == COLLoadErrorDialog.ABORT:
                        img_debugger.info("Load aborted by user")
                        return None
                    elif action == COLLoadErrorDialog.SKIP_ALL:
                        skip_all_errors = True
                        img_debugger.info("Skipping all errors")
                        progress.add_warning(f"Skipped: {model_name} ({str(e)[:50]})")
                    elif action == COLLoadErrorDialog.IGNORE_ALL:
                        ignore_all_errors = True
                        img_debugger.info("Ignoring all errors")
                    elif action == COLLoadErrorDialog.SKIP:
                        progress.add_warning(f"Skipped: {model_name} ({str(e)[:50]})")
                    # IGNORE: just continue
                elif skip_all_errors:
                    progress.add_warning(f"Skipped: {model_name} ({str(e)[:50]})")
                # ignore_all: just continue silently
        
        # Done
        col_file.is_loaded = len(col_file.models) > 0
        progress.set_progress(100)
        
        # Final summary
        loaded = len(col_file.models)
        total_found = len(signatures)
        skipped = total_found - loaded
        
        if skipped > 0:
            progress.set_status(f"Loaded {loaded}/{total_found} models ({skipped} skipped)")
        else:
            progress.set_status(f"Loaded {loaded} models successfully")
        
        QApplication.processEvents()
        
        return col_file if col_file.is_loaded else None
        
    except Exception as e:
        img_debugger.error(f"Archive load error: {str(e)}")
        return None


__all__ = ['load_col_with_progress']
