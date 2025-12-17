# COL Workshop - Action Plan
# Current file: col_workshop.py (5430 lines)

## Current State
✅ Old parsing code ALREADY REMOVED (you did this earlier)
✅ Old data structures ALREADY REMOVED (Vector3, COLModel, etc.)
✅ GUI code is CLEAN

## What Remains
❌ Missing imports for COLFile, COLModel, COLVersion, Vector3
❌ References throughout GUI code that will crash without classes

## Files Ready to Copy
✅ methods/col_data_structures.py - Pure data classes
✅ methods/col_parser.py - Complete parser (COL1/2/3)
✅ methods/col_file.py - High-level COLFile interface

---

## Option A: Quick Fix (Temporary Stubs)

Add this after line 46 in col_workshop.py:

```python
# ===== TEMPORARY STUBS - Remove after copying methods/ files =====
class Vector3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x, self.y, self.z = float(x), float(y), float(z)

class COLVersion:
    COL_1, COL_2, COL_3 = 1, 2, 3
    def __init__(self, value):
        self.value = value
        self.name = f"COL{value}"

class COLModel:
    def __init__(self):
        self.name = "Unknown"
        self.version = COLVersion(1)
        self.model_id = 0
        self.spheres, self.boxes, self.vertices, self.faces = [], [], [], []
        self.bounding_box = None

class COLFile:
    def __init__(self, file_path=None):
        self.file_path = file_path
        self.models, self.is_loaded, self.load_error = [], False, None
    def load_from_file(self, path):
        self.load_error = "Parser not yet implemented"
        return False
# ===== END STUBS =====
```

**Result:** File runs, but can't load COL files yet

---

## Option B: Full Integration (Recommended)

### Step 1: Copy methods files
```bash
cp /home/claude/col_workshop_rebuild/methods/col_data_structures.py ~/Col-Workshop/apps/methods/
cp /home/claude/col_workshop_rebuild/methods/col_parser.py ~/Col-Workshop/apps/methods/
cp /home/claude/col_workshop_rebuild/methods/col_file.py ~/Col-Workshop/apps/methods/
```

### Step 2: Update imports in col_workshop.py
Replace line ~42 area with:

```python
# Import project modules AFTER path setup
from apps.methods.svg_icon_factory import SVGIconFactory

# Import COL data structures and parser
from apps.methods.col_data_structures import (
    Vector3, COLVersion, BoundingBox, COLSphere, COLBox,
    COLVertex, COLFace, COLModel
)
from apps.methods.col_file import COLFile
```

**Result:** File runs AND can load COL files correctly

---

## No Lines to Delete!

You asked about "lines 4373 onwards" - but there's nothing to delete.
Everything from line 1-5430 is GUI code that just needs proper imports.

---

## What Changed from Before

**OLD (broken):**
- Had Vector3, COLModel, etc. defined somewhere (already removed)
- Had broken parser that didn't handle COL2/3 compression
- Stretched geometry, missing faces

**NEW (working):**
- Data structures in methods/col_data_structures.py
- Proper parser with fixed-point conversion (÷128.0)
- GTA Wiki spec compliant
- Handles COL1/2/3 correctly

---

## Testing After Integration

```python
# This should work:
workshop = COLWorkshop()
col_file = COLFile()
if col_file.load_from_file("test.col", debug=True):
    print(f"Loaded {len(col_file.models)} models")
    workshop.display_col_file(col_file)
```

---

## Which Option?

**Option A:** Quick fix to make it run (add stubs)
**Option B:** Full working solution (copy files + update imports)

Which do you want?
