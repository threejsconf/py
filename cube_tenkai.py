import bpy

# 元キューブ
# ---　角かっこ内書き換え必須です　------
source = bpy.data.objects["Example.001"]
# ------------------------------------
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

# ------------------------------------
# 以下：覚書
# ------------------------------------

# ターミナルで

# cd ~/Documents/BlenderScripts/
# git clone https://github.com/threejsconf/py/edit/main/cube_tenkai.py

# ------------------------------------

# Blenderから bpy を使って直接実行：

# import urllib.request
# url = "https://raw.githubusercontent.com/threejsconf/py/main/cube_tenkai.py"
# exec(urllib.request.urlopen(url).read())

# ------------------------------------

# --- 使用時の注意点 ---
# 1. 立方体は必ず「スケール適用」(Ctrl+A → Scale) してから使う。
# 2. source は正方形のキューブ前提（dimensions.x = y = z）。デフォルト。
# 3. 展開面は Z=0 に配置され、テクスチャ焼きに適している。


