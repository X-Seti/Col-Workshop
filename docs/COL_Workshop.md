# COL Workshop

Standalone COL editor, synced from IMG Factory 1.6.

## Starting
- `python3 launch_col_workshop.py`
- Open a .col with Open, Ctrl+O, or drag it onto the window.
- Dropping a .col on an open file asks: Add to current, Open in new tab, Cancel.

## Window layout
| Area | Contents |
|------|----------|
| Left pane | COL Models list (preview + details), Surface Data tab |
| Centre | 3D viewport, ribbon toolbars |
| Right | Transform, navigation, render and paint ribbons, model name and version |

- Drag the splitter grips to resize; positions are saved.
- Buttons switch to icon-only when a pane is narrow.
- Ribbons can be moved, hidden or reassigned (right-click a ribbon, or Ribbon Manager).

## Supported formats
| Version | Games | Notes |
|---------|-------|-------|
| COL1 (COLL) | GTA III, VC | 35 surface materials |
| COL2 (COL2) | SA (PS2) | face groups, int16 vertices |
| COL3 (COL3) | SA (PC) | adds shadow mesh |
| COL4 (COL4) | SA (unused) | read and write |

SA archives may mix COL2 and COL3 models; each keeps its own version.

## Editing models
- Select a model in the list to show it in the viewport.
- Rename: F2. Duplicate: Ctrl+D. Delete: Del. Copy/paste: Ctrl+C / Ctrl+V.
- Right-click a model for export, import-replace, rename, details.
- Mesh editor: edit vertices and faces of the selected model.
- Shadow mesh (COL3): view, create from mesh, remove.
- Undo: Ctrl+Z.

## Converting versions
Right panel: convert button, then choose COL1, COL2 or COL3.
- Crossing COL1 <-> COL2/3 shows a table of used surfaces.
- Each row: count, current surface, target surface (editable).
- Targets default to the nearest name, then the same group (road, grass, metal...).
- SA -> COL1 remembers each original SA surface; converting back restores them
  (until the workshop closes).
- Vehicle windscreen flag is mapped (SA 19, VC 17).
- COL2/3 -> COL1 drops face groups, shadow mesh and lines.
- Changes save on Save.

## Damaged files
Records that cannot be read are skipped on load (status bar shows the count).
Save asks first, as skipped records are not written.

## Edit tools (Edit ribbon, or right-click a face)
Select faces in the viewport (click, Ctrl+click adds, drag to paint-select).
With nothing selected, gizmo and scale work on the whole model.
| Tool | Action |
|------|--------|
| Gizmo G / R / S | Move, rotate, scale the selection; drag an arrow, ring or square |
| Detach | Split selected faces from neighbours so they move without stretching others |
| Selection to New Model | Copy or move faces into a new model in this file |
| Save Selection as COL | Copy or move faces into a new .col file |
| Delete Selected Faces | Remove faces (unused vertices removed) |
| Vertex Select Mode + Weld | Pick 2+ vertices, join them into one |
| Fill Hole | Select the faces around a hole; the gap is filled |
| Box / Sphere to Mesh | Replace a box or sphere with triangles |
| Faces to Box / Sphere | Replace selected faces with an enclosing box or sphere |
| Scale... / Centre to Origin | Numeric scale; move model centre to 0,0,0 |
| Merge COL Files | Add every model from other COL files |
All edits undo with Ctrl+Z; bounds are rebuilt after each edit.

## Shadow mesh (COL3)
Shadow Mesh ribbon: View toggles a magenta overlay, Create copies the mesh
(offers COL3 upgrade), Remove deletes it. Saved with the model.

## Game controller (PS5 DualSense)
Edit ribbon: Game Controller toggle (needs pygame; remembered).
| Control | Action |
|---------|--------|
| Right stick / L2 R2 | Orbit / zoom |
| Left stick | Pan, or move the grabbed selection |
| Cross | Select face under the crosshair; again to grab; again to drop |
| Square | Add/remove face under crosshair |
| Circle | Cancel grab / clear selection |
| Triangle | Move / Rotate / Scale |
| L1 / R1 | Axis: free, X, Y, Z |
| D-pad | Up/down next model (Z while grabbing); left/right 15 deg while rotating |
| Options / Create / Touchpad | Render style / undo / fit view |
| L3 / R3 | Fine speed / vertex mode |

## Surface Data tab
Opens and edits surface.dat: adhesion, friction, wheel effect, audio,
per-surface flags. Add, Del, Dup manage entries.

## Viewport keys
| Key | Action |
|-----|--------|
| G | Move gizmo |
| R | Rotate gizmo |
| F | Fit to window (fill faces in paint mode) |
| V | Cycle wireframe / semi / solid |
| Esc | Leave paint mode |
| Mouse | Left drag pan, right or middle drag rotate, wheel zoom, right-click view presets |

## Hotkeys
| Key | Action |
|-----|--------|
| Ctrl+O / Ctrl+S / Ctrl+Shift+S | Open / Save / Save as |
| Alt+Shift+S | Force save |
| Ctrl+Z | Undo |
| Ctrl+C / Ctrl+V / Del | Copy / paste / delete model |
| Ctrl+D / F2 | Duplicate / rename (type in name field, Enter) |
| Ctrl+I / Ctrl+E / Ctrl+Shift+E | Import / export selected / export all |
| Ctrl+A / Ctrl+Shift+I / Ctrl+F | Select all / invert / find |
| F5 | Refresh |
| Alt+Enter | Model details |
| F1 | Help and about |

Hotkeys can be changed in Settings.

## Settings files
- Source run: `~/.config/imgfactory/` (col_workshop.json: ribbon layout, splitter sizes).
- Windows exe: `settings/` folder beside `Col_Workshop.exe`, theme settings included (portable; keep the folder writable). First run copies the bundled defaults there.
- Themes: `apps/themes/*.json`.

## Code layout
| File | Contents |
|------|----------|
| `apps/components/Col_Editor/col_workshop.py` | COLWorkshop: init, settings, docking, help, theme, tabs |
| `.../depends/col_setup_ui_func.py` | COLSetupUIMixin: panels, ribbons, menus, hotkeys, theme, status |
| `.../depends/col_core_logic_func.py` | COLCoreLogicMixin: load/save, import/export, surface, shadow, drag and drop |
| `.../depends/col_list_func.py` | COLListMixin: model list, selection, previews, thumbnails, info |
| `.../depends/col_paint_func.py` | COLPaintMixin: face material painting |
| `.../depends/col_edit_func.py` | COLEditMixin: edit tools, controller toggle |
| `.../depends/col_win_func.py` | COLWindowMixin: frameless window, resize, splitters, move mode |
| `.../depends/col_viewport.py` | COL3DViewport (QPainter preview) |
| `.../col_mesh_editor.py` | Mesh editor dialog |
| `apps/methods/col_workshop_*.py` | COL classes, parser, loader, writer |
| `apps/methods/col_splice.py` | Byte-identical save of unedited models |
| `apps/methods/col_materials.py` | Surface tables, GTA3/VC <-> SA conversion |
| `apps/methods/grip_splitter.py` | Splitter with ribbon-style grip |
| `apps/methods/col_mesh_ops.py` | Geometry edits (detach, weld, fill, convert, scale) |
| `apps/methods/gamepad_input.py` | Game controller reader (pygame) |
