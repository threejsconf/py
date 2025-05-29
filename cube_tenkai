import bpy

# 元キューブ
source = bpy.data.objects["Cube.002"]
size = source.dimensions.x
spacing = 0.01
unit = size + spacing

# 既存のFace_を削除
for obj in bpy.data.objects:
    if obj.name.startswith("Face_"):
        bpy.data.objects.remove(obj, do_unlink=True)

# 指定された配置
positions = {
    "Back":   (0, 0),            # 中心
    "Top":    (0,  unit),        # 上
    "Bottom": (0, -unit),        # 下
    "Left":   (-unit, 0),        # 左
    "Right":  (unit, 0),         # 右
    "Front":  (0, -2*unit),      # 最下部（正面）
}

# 各面作成（Z=0に配置）
for face, (x, y) in positions.items():
    bpy.ops.mesh.primitive_plane_add(
        size=size,
        location=(
            source.location.x + x,
            source.location.y + y,
            0  # Z=0で固定
        )
    )
    obj = bpy.context.object
    obj.name = f"Face_{face}"
