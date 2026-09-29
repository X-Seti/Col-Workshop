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
| Ctrl+D / F2 | Duplicate / rename |
| Ctrl+I / Ctrl+E / Ctrl+Shift+E | Import / export / export all |
| Ctrl+A / Ctrl+F | Select all / find |
| F5 | Refresh |
| Alt+Enter | Model details |

Hotkeys can be changed in Settings.

## Settings files
- `~/.config/imgfactory/col_workshop.json`: ribbon layout, splitter sizes.
- Themes: `apps/themes/*.json`.

## Code layout
| File | Contents |
|------|----------|
| `apps/components/Col_Editor/col_workshop.py` | COLWorkshop window, docking, dialogs, list |
| `.../depends/col_setup_ui_func.py` | COLSetupUIMixin: panels, ribbons, menus, hotkeys, theme |
| `.../depends/col_core_logic_func.py` | COLCoreLogicMixin: load/save, import/export, edits, undo |
| `.../depends/col_win_func.py` | COLWindowMixin: frameless window, resize, splitters |
| `.../depends/col_viewport.py` | COL3DViewport (QPainter preview) |
| `.../col_mesh_editor.py` | Mesh editor dialog |
| `apps/methods/col_workshop_*.py` | COL classes, parser, loader, writer |
| `apps/methods/col_splice.py` | Byte-identical save of unedited models |
| `apps/methods/col_materials.py` | Surface tables, GTA3/VC <-> SA conversion |
| `apps/methods/grip_splitter.py` | Splitter with ribbon-style grip |
