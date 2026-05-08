import bpy
import bmesh

# 全局变量，用于存储翻转法线面的数量，以便在UI中显示
flipped_face_count = 0

def detect_flipped_normals_logic(obj):
    """
    检测 Blender mesh 对象中可能存在的翻转法线面（flipped normals faces）。
    通过与 Blender 内置的“向外重计算法线”结果进行对比来判断。

    Args:
        obj (bpy.types.Object): 当前选中的 mesh 对象。

    Returns:
        list: 包含所有疑似翻转法线面的 face index 列表。
    """
    flipped_faces = []

    if not obj or obj.type != 'MESH':
        return flipped_faces

    mesh = obj.data
    bm_original = bmesh.new()
    bm_original.from_mesh(mesh)
    bm_original.faces.ensure_lookup_table()

    bm_recalc = bmesh.new()
    bm_recalc.from_mesh(mesh)
    bm_recalc.faces.ensure_lookup_table()

    # 在副本上执行 Blender 内置的“向外重计算法线”
    bmesh.ops.recalc_face_normals(bm_recalc, faces=bm_recalc.faces)

    for i, face_orig in enumerate(bm_original.faces):
        face_recalc = bm_recalc.faces[i]
        dot_product = face_orig.normal.dot(face_recalc.normal)

        if dot_product < -0.999:
            flipped_faces.append(face_orig.index)

    bm_original.free()
    bm_recalc.free()

    return flipped_faces

def highlight_flipped_faces_logic(obj, flipped_faces):
    """
    在 Blender 中自动选中并高亮检测到的翻转法线面。

    Args:
        obj (bpy.types.Object): 当前 mesh 对象。
        flipped_faces (list): 包含问题 face index 的列表。
    """
    if not obj or obj.type != 'MESH':
        return

    original_mode = obj.mode
    original_select_mode = bpy.context.tool_settings.mesh_select_mode[:]

    try:
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.context.tool_settings.mesh_select_mode = (False, False, True) # 顶点, 边, 面

        bm = bmesh.from_edit_mesh(obj.data)
        bm.faces.ensure_lookup_table()

        # 清除当前所有选择
        for elem in (*bm.verts, *bm.edges, *bm.faces):
            elem.select = False

        for face_idx in flipped_faces:
            if face_idx < len(bm.faces):
                bm.faces[face_idx].select = True

        bmesh.update_edit_mesh(obj.data)

    finally:
        bpy.ops.object.mode_set(mode=original_mode)
        bpy.context.tool_settings.mesh_select_mode = original_select_mode


class FUM_OT_DetectFlippedNormals(bpy.types.Operator):
    """检测并高亮显示模型中的翻转法线面"""
    bl_idname = "fum.detect_flipped_normals"
    bl_label = "检测翻转法线"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        global flipped_face_count
        flipped_face_count = 0 # 重置计数

        obj = context.active_object

        if not obj or obj.type != 'MESH':
            self.report({'WARNING'}, "请选择一个网格对象。")
            return {'CANCELLED'}

        # 调用检测逻辑
        flipped_faces = detect_flipped_normals_logic(obj)
        flipped_face_count = len(flipped_faces)

        # 调用高亮逻辑
        if flipped_face_count > 0:
            highlight_flipped_faces_logic(obj, flipped_faces)
            self.report({'INFO'}, f"检测到 {flipped_face_count} 个翻转法线面，已高亮显示。")
        else:
            self.report({'INFO'}, "未检测到翻转法线面。")

        return {'FINISHED'}
