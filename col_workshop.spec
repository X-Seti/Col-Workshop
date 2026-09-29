# -*- mode: python ; coding: utf-8 -*-
#this belongs in root /col_workshop.spec - Version: 1
# X-Seti - Sept 29 2026 - Col Workshop - PyInstaller build spec (Windows)

"""
PyInstaller spec for the standalone COL Workshop Windows build.
Build: pyinstaller col_workshop.spec  ->  dist/Col_Workshop/Col_Workshop.exe
"""

##Methods list -
# _app_data

import os

ROOT = os.path.abspath(SPECPATH)


def _app_data(): #vers 1
    """Every non-Python file under apps/, kept at the same relative path."""
    out = []
    for base, dirs, files in os.walk(os.path.join(ROOT, 'apps')):
        dirs[:] = [d for d in dirs if d != '__pycache__']
        for name in files:
            if name.endswith(('.py', '.pyc', '.log')):
                continue
            src = os.path.join(base, name)
            out.append((src, os.path.relpath(base, ROOT)))
    return out


a = Analysis(
    ['launch_col_workshop.py'],
    pathex=[ROOT],
    binaries=[],
    datas=_app_data() + [(os.path.join(ROOT, 'appfactory.settings.json'), '.')],
    hiddenimports=['PyQt6.QtSvg', 'PyQt6.QtOpenGL', 'PyQt6.QtOpenGLWidgets',
                   'OpenGL.platform.win32', 'OpenGL.arrays.numpymodule'],
    excludes=['tkinter'],
    noarchive=False,
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz, a.scripts, [],
    exclude_binaries=True,
    name='Col_Workshop',
    console=False,
    upx=False,
)
coll = COLLECT(exe, a.binaries, a.datas, upx=False, name='Col_Workshop')
