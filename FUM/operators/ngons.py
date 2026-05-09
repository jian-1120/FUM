import bpy
import bmesh

# 全局变量，用于存储 N-Gon 的数量，以便在 UI 中显示
ngon_count = 0

def detect_ngons_logic(obj):
    """
    检测 Blender mesh 对象中所有边数大于 4 的面（N-Gons）。

    Args:
        obj (bpy.types.Object): 当前选中的 mesh 对象。

    Returns:
        list: 包含所有 N-Gon faces 的 index 列表。
    """
    ngon_faces = []

    if not obj or obj.type != 'MESH':
        return ngon_faces

    # 获取 mesh 数据并创建 BMesh
    mesh = obj.data
    bm = bmesh.new()
    bm.from_mesh(mesh)
    bm.faces.ensure_lookup_table()

    # 遍历所有面，检测边数大于 4 的面
    for face in bm.faces:
        if len(face.verts) > 4:
            ngon_faces.append(face.index)

    # 释放 BMesh 资源
    bm.free()

    return ngon_faces

def highlight_ngon_faces_logic(obj, ngon_faces):
    """
    在 Blender 中自动选中并高亮检测到的 N-Gon faces。

    Args:
        obj (bpy.types.Object): 当前 mesh 对象。
        ngon_faces (list): 包含 N-Gon face index 的列表。
    """
    if not obj or obj.type != 'MESH':
        return

    # 保存当前模式，以便操作完成后恢复
    original_mode = obj.mode
    original_select_mode = bpy.context.tool_settings.mesh_select_mode[:]

    try:
        # 切换到编辑模式
        bpy.ops.object.mode_set(mode='EDIT')

        # 切换到面选择模式
        bpy.context.tool_settings.mesh_select_mode = (False, False, True) # 顶点, 边, 面

        # 获取 BMesh 数据
        bm = bmesh.from_edit_mesh(obj.data)
        bm.faces.ensure_lookup_table()

        # 清除当前所有选择
        for elem in (*bm.verts, *bm.edges, *bm.faces):
            elem.select = False

        # 选中所有 N-Gon faces
        for face_idx in ngon_faces:
            if face_idx < len(bm.faces):
                bm.faces[face_idx].select = True

        # 更新视图以显示选择
        bmesh.update_edit_mesh(obj.data)

    finally:
        # 恢复到原始模式和选择模式
        bpy.ops.object.mode_set(mode=original_mode)
        bpy.context.tool_settings.mesh_select_mode = original_select_mode


class FUM_OT_DetectNGons(bpy.types.Operator):
    """检测并高亮显示模型中的 N-Gons（边数 > 4 的面）"""
    bl_idname = "fum.detect_ngons"
    bl_label = "检测 N-Gons"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        global ngon_count
        ngon_count = 0 # 重置计数

        obj = context.active_object

        # 安全检查：确保选中了网格对象
        if not obj or obj.type != 'MESH':
            self.report({'WARNING'}, "请选择一个网格对象。")
            return {'CANCELLED'}

        # 调用检测逻辑
        ngon_faces = detect_ngons_logic(obj)
        ngon_count = len(ngon_faces)

        # 调用高亮逻辑
        if ngon_count > 0:
            highlight_ngon_faces_logic(obj, ngon_faces)
            self.report({'INFO'}, f"检测到 {ngon_count} 个 N-Gons，已高亮显示。")
        else:
            self.report({'INFO'}, "未检测到 N-Gons。")

        return {'FINISHED'}
