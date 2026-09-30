# Col-Workshop

Collision (COL) editor for RenderWare GTA games: GTA III, Vice City, San Andreas.
Standalone build of the COL Workshop from [IMG Factory 1.6](https://github.com/X-Seti/Img-Factory-1.6).

## Features
- Open COL1, COL2, COL3 and COL4 archives, loose or inside IMG archives.
- Mixed-version archives (SA) load and save unchanged.
- Unedited models save byte-identical; edited models are rewritten.
- 3D preview: wireframe, semi, solid; move/rotate gizmo; face painting.
- Edit spheres, boxes, mesh vertices and faces; shadow mesh create/remove.
- Convert models between COL1, COL2 and COL3 with surface mapping
  (GTA III/VC 35 surfaces <-> SA 179 surfaces).
- surface.dat editor (Surface Data tab).
- Import/export single models, IDE-driven import/export, build COL from TXD.
- Drag and drop .col files; add to the open file or open in a new tab.
- Themes, ribbon toolbars, custom hotkeys, compact icon-only buttons.

## Requirements
- Python 3.10+
- PyQt6
- numpy (3D viewport), PyOpenGL (optional GL viewport)

```
pip install PyQt6 numpy PyOpenGL
```

## Run
```
python3 launch_col_workshop.py
```

## Windows build
GitHub Actions (`.github/workflows/windows-build.yml`) builds `Col_Workshop.exe`
with PyInstaller (`col_workshop.spec`) on every push to main, or by hand from the
Actions tab. Download `Col_Workshop_Windows.zip` from the `windows-build` release
(or the Actions artifact): a folder with the exe, Qt DLLs, plugins, themes and
settings. Run `Col_Workshop.exe`. Each build is also committed to the repo root
(`Col_Workshop.exe`, `_internal/`), with `settings/` as the shipped defaults.

## Documentation
See [docs/COL_Workshop.md](docs/COL_Workshop.md).

## Credits
X-Seti. See Credits.md. License: see LICENSE.
