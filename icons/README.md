#this belongs in icons/README.md - Version: 2
# X-Seti - September30 2026 - COL Workshop - Icons

# COL Workshop Icons

The app draws all icons as SVG (apps/methods/imgfactory_svg_icons.py).
This folder is for community PNG / JPG / SVG replacements.
Apply one: Ribbon Manager, select an action, Set Icon... (Reset Icon restores the SVG).
Choices save in col_workshop.json and in ribbon presets.

## Wanted
Colourful 3ds Max style icons.
Flat, Stylish, digital, other styles

## Format
- PNG with transparency (JPG accepted), 64x64 master, also 32x32 and 20x20 if possible.
- File name = action name below, e.g. `box_to_mesh_64.png`.
- Readable on light and dark themes.

## Priority: edit tools sharing an icon
| File name | Action | Current SVG |
|-----------|--------|-------------|
| box_to_mesh | Box to Mesh | box_icon |
| sphere_to_mesh | Sphere to Mesh | sphere_icon |
| faces_to_box | Faces / Mesh to Box | mesh_icon |
| faces_to_sphere | Faces / Mesh to Sphere | shading_sphere_icon |
| detach | Detach Selected Faces | poly_select_icon |
| selection_to_model | Selection to New Model | new_icon (shared with New) |
| selection_to_col | Save Selection as COL | export_icon (shared with Export) |
| merge_col | Merge COL Files | import_icon (shared with Import) |
| delete_faces | Delete Selected Faces | delete_icon (shared with Delete) |
| weld | Weld Selected Vertices | converge_to_center_icon |
| fill_hole | Fill Hole | fill_icon |
| optimise_mesh | Optimise Mesh | filter_icon |
| scale | Scale | bounds_icon |
| scale_gizmo | Scale Gizmo | dp_resize_icon |
| centre_origin | Centre to Origin | snap_to_center_icon |
| vertex_mode | Vertex Select Mode | vertex_select_icon |
| shadow_mesh | Create / Remove / Show Shadow Mesh | none |
| controller | Game Controller | controller_icon |

## Other icons used (same name as the SVG function, without `_icon`)
add, analyze, arrow_down, arrow_left, arrow_right, arrow_up, backface, build,
checkerboard, close, col_workshop, color_picker, compress, convert, copy,
dropper, duplicate, fit, flip_horz, flip_vert, folder, info, maximize, minimize,
open, package, paint, paste, properties, reset, rotate_ccw, rotate_cw, save,
saveas, search, settings, surfaceedit, trash, uncompress, undo, undo_paint,
view, zoom_in, zoom_out
