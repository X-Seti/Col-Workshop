"""
GTA RenderWare .COL collision file analyser

Goal:
- Parse and split COL headers and sections
- Expose structured data usable for a future COL editor

Supports:
- COL v1 / v2 / v3 (basic layout awareness)
- RW-style binary parsing

This is an ANALYSER, not a full editor yet.
"""

import struct
from dataclasses import dataclass
from typing import List, BinaryIO

# -----------------------------
# Low-level helpers
# -----------------------------

def read(fmt: str, fh: BinaryIO):
    size = struct.calcsize(fmt)
    data = fh.read(size)
    if len(data) != size:
        raise EOFError("Unexpected EOF")
    return struct.unpack(fmt, data)

# -----------------------------
# Data structures
# -----------------------------

@dataclass
class ColHeader:
    magic: str
    version: int
    model_name: str
    file_size: int
    sphere_count: int
    box_count: int
    face_count: int
    line_count: int
    flags: int

@dataclass
class ColSphere:
    radius: float
    center: tuple
    surface: int

@dataclass
class ColBox:
    min: tuple
    max: tuple
    surface: int

@dataclass
class ColFace:
    a: int
    b: int
    c: int
    surface: int

# -----------------------------
# Header parsing
# -----------------------------

def parse_header(fh: BinaryIO) -> ColHeader:
    magic = fh.read(4).decode('ascii', errors='ignore')
    if magic != 'COLL':
        raise ValueError("Not a COL file")

    version, = read('<I', fh)
    model_name = fh.read(22).split(b'\x00', 1)[0].decode('ascii', 'ignore')
    fh.read(2)  # padding

    file_size, = read('<I', fh)
    sphere_count, = read('<H', fh)
    box_count, = read('<H', fh)
    face_count, = read('<H', fh)
    line_count, = read('<H', fh)
    flags, = read('<I', fh)

    return ColHeader(
        magic=magic,
        version=version,
        model_name=model_name,
        file_size=file_size,
        sphere_count=sphere_count,
        box_count=box_count,
        face_count=face_count,
        line_count=line_count,
        flags=flags
    )

# -----------------------------
# Section parsing
# -----------------------------

def parse_spheres(fh, count) -> List[ColSphere]:
    spheres = []
    for _ in range(count):
        radius, = read('<f', fh)
        x, y, z = read('<3f', fh)
        surface, = read('<H', fh)
        fh.read(2)  # padding
        spheres.append(ColSphere(radius, (x, y, z), surface))
    return spheres


def parse_boxes(fh, count) -> List[ColBox]:
    boxes = []
    for _ in range(count):
        minx, miny, minz = read('<3f', fh)
        maxx, maxy, maxz = read('<3f', fh)
        surface, = read('<H', fh)
        fh.read(2)
        boxes.append(ColBox((minx, miny, minz), (maxx, maxy, maxz), surface))
    return boxes


def parse_faces(fh, count) -> List[ColFace]:
    faces = []
    for _ in range(count):
        a, b, c = read('<3H', fh)
        surface, = read('<H', fh)
        faces.append(ColFace(a, b, c, surface))
    return faces

# -----------------------------
# High-level API
# -----------------------------

def analyse_col(path: str):
    with open(path, 'rb') as fh:
        header = parse_header(fh)

        spheres = parse_spheres(fh, header.sphere_count)
        boxes = parse_boxes(fh, header.box_count)
        faces = parse_faces(fh, header.face_count)

        return {
            "header": header,
            "spheres": spheres,
            "boxes": boxes,
            "faces": faces,
        }


if __name__ == '__main__':
    import sys
    data = analyse_col(sys.argv[1])
    print(data['header'])
