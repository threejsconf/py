import bpy

# 展開元のキューブ名
# --- ダブルクォート内書き換え必須 ------
source_name = "Example.002"
# ------------------------------------
source = bpy.data.objects.get(source_name)
if not source:
    raise Exception(f"オブジェクト {source_name} が見つかりません")

# キューブのサイズと間隔
size = source.dimensions.x
spacing = 0.01
unit = size + spacing

# マテリアル取得（存在しなければ警告）
material = source.active_material
if not material:
    raise Exception(f"{source_name} にマテリアルがありません")

# 既存の Face_ を削除
for obj in bpy.data.objects:
    if obj.name.startswith("Face_"):
        bpy.data.objects.remove(obj, do_unlink=True)

# 展開レイアウト
positions = {
    "Back":   (0, 0),
    "Top":    (0,  unit),
    "Bottom": (0, -unit),
    "Left":   (-unit, 0),
    "Right":  (unit, 0),
    "Front":  (0, -2*unit),
}

# プレーン作成とマテリアル複製適用
for face, (x, y) in positions.items():
    bpy.ops.mesh.primitive_plane_add(
        size=size,
        location=(source.location.x + x, source.location.y + y, 0)
    )
    obj = bpy.context.object
    obj.name = f"Face_{face}"
    # マテリアルのコピーを貼り付け
    mat_copy = material.copy()
    obj.data.materials.append(mat_copy)
