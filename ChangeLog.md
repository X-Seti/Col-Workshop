#this belongs in root /ChangeLog.md - Col-Workshop

## March 2026 — Major viewport overhaul, full mesh/box/sphere editing

### Build 161 — Fix viewport rendering on model click
- `_select_model_by_row` used directly on file load — no longer calls
  `_on_collision_selected` which read from hidden detail table
- `set_current_model` resets pan/zoom so each model is always centred

### Build 160 — Three bug fixes
- Bug 1: `table.setVisible(True)` called without None guard fixed
- Bug 2: `open_col_editor(entry)` now accepts optional entry param
- Bug 3: COL2/3 parser completely rewritten — was treating offset-table
  layout as sequential COL1 counts. COL2/3 uses uint16 counts + 9x uint32
  offsets relative to block base. Spheres, boxes, verts, faces now parsed.

### Build 159 — Fix preview not updating on model click
- Three stacked bugs: compact list read selection from hidden table,
  model index read from wrong column after Build 157, thumbnail spin
  tried to set DecorationRole on text cell. All fixed via unified
  `_select_model_by_row(row)`.

### Build 158 — Remove 200-model hard cap in loader
- `col_workshop_loader.py` had hardcoded limit of 200 models
- generics.col has 1146 models — 946 were silently dropped

### Build 157 — Fix Type vs Version columns
- Type = fourcc (COLL/COL2/COL3/COL4), Version = game target
  (GTA III/VC, SA PS2, SA PC/Xbox)

### Build 156 — SVG icons on non-zero counts in detail table
- Spheres/Boxes/Vertices/Faces columns show SVG icon when count > 0
- 14px icons: sphere (cyan), box (yellow), dot-cluster (green), mesh (blue)

### Build 155 — Detail table: 8 proper columns, no thumbnail
- Columns: Model Name, Type, Version, Size (bounds radius),
  Spheres, Boxes, Vertices, Faces. Row height 22px.

### Build 154 — [=] compact view: custom delegate
- COLCompactDelegate draws each row: name | COL type badge | 4 icon badges
- COL type colour-coded: COL1=blue COL2=green COL3=yellow COL4=purple
- 4 icon badges: vertex dots, face triangle, sphere ring, box cube

### Build 153 — Compact list single-row stats layout
- Name + version (left), 4 icon badges inline (right)
- No thumbnail in [=] view

### Build 152 — Thumbnail right-click: view axis menu
- Right-click on either list: Thumbnail View submenu
- Top/Front/Side/Isometric/Bottom/Back — regenerates all thumbnails

### Build 151 — Fix model selection (unified _select_model_by_row)
- Both list handlers delegate to `_select_model_by_row(row)`

### Build 150–149 — Startup crash fix + debug prints
- Fix: preview_widget not yet created when nav buttons connect
- Use lambdas for deferred lookup

### Build 148 — Proper box/sphere/bounds rendering + render modes
- Boxes: 8 corners projected, 12 AABB edges drawn
- Spheres: 3 projected rings (XY/XZ/YZ), 48 segments each
- Bounds AABB: dashed purple, bounding sphere: dotted purple
- Render modes: Wireframe / Semi / Solid — V key, right-click, button
- Left nav buttons all wired up

### Build 147 — Full COL mesh editing
- Viewport click-to-select faces and vertices
- Keyboard: Del, Ctrl+A, Ctrl+Z, Ctrl+D
- Flip Face(s), Select Connected (BFS), Merge Close Vertices
- Right-click context menu in viewport

### Build 145 — Full COL editing: boxes/spheres/bounds + gizmo fix
- Gizmo translate/rotate moves ALL geometry (verts, boxes, spheres, bounds)
- Mesh Editor: 4 tabs — Mesh, Boxes, Spheres, Bounds
- Recalculate Bounds from geometry

### Build 144 — ChangeLog v29

### Build 143 — COL3DViewport fully self-contained
- paintEvent draws everything directly, no workshop roundtrip
- Rotation, zoom, pan all work reliably

### Builds 137–142 — COL Mesh Editor + XYZ gizmo + viewport fixes
- COLMeshEditor with face/vertex tables, 71 GTA materials, undo
- Reference grid, XYZ gizmo with translate/rotate modes
- Fixed zoom not affecting mesh, fixed locked view
- Middle mouse = rotate, left = pan, scroll = zoom
