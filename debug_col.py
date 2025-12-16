# Debug script - run in Col Workshop
# Print first model's data to verify parsing

if hasattr(self, 'current_col_file') and self.current_col_file:
    model = self.current_col_file.models[0]
    print(f"Model: {model.name}")
    print(f"Vertices: {len(model.vertices)}")
    if model.vertices:
        v = model.vertices[0]
        print(f"First vertex type: {type(v.position)}")
        print(f"First vertex: {v.position.x}, {v.position.y}, {v.position.z}")
    print(f"Boxes: {len(model.boxes)}")
    if model.boxes:
        b = model.boxes[0]
        print(f"First box min type: {type(b.min_point)}")
        print(f"First box min: {b.min_point.x}, {b.min_point.y}, {b.min_point.z}")
        print(f"First box max: {b.max_point.x}, {b.max_point.y}, {b.max_point.z}")
