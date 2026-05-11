import bpy
import bmesh

# 全局变量用于存储检测结果数量，供 UI 面板显示
isolated_vertex_count = 0

def detect_isolated_vertices_logic(obj):
    """
    检测网格中的孤立顶点逻辑。
    孤立顶点定义：不连接任何边或面的顶点。
    """
    isolated_indices = []
    
    if not obj or obj.type != 'MESH':
        return isolated_indices

    # 创建 BMesh 副本进行检测
    bm = bmesh.new()
    bm.from_mesh(obj.data)
    bm.verts.ensure_lookup_table()

    for v in bm.verts:
        # 如果顶点没有连接的边，则判定为孤立顶点
        if len(v.link_edges) == 0:
            isolated_indices.append(v.index)

    bm.free()
    return isolated_indices

def highlight_isolated_vertices_logic(obj, isolated_indices):
    """
    在编辑模式下高亮选中孤立顶点。
    """
    if not obj or obj.type != 'MESH':
        return

    # 切换到编辑模式
    if obj.mode != 'EDIT':
        bpy.ops.object.mode_set(mode='EDIT')

    # 切换到顶点选择模式
    bpy.context.tool_settings.mesh_select_mode = (True, False, False)

    # 获取编辑模式下的 BMesh
    bm = bmesh.from_edit_mesh(obj.data)
    bm.verts.ensure_lookup_table()

    # 清除当前选择
    for v in bm.verts:
        v.select = False
    for e in bm.edges:
        e.select = False
    for f in bm.faces:
        f.select = False

    # 选中孤立顶点
    for idx in isolated_indices:
        if idx < len(bm.verts):
            bm.verts[idx].select = True

    # 更新视图
    bmesh.update_edit_mesh(obj.data)

class FUM_OT_DetectIsolatedVertices(bpy.types.Operator):
    """检测并高亮显示模型中的孤立顶点"""
    bl_idname = "fum.detect_isolated_vertices"
    bl_label = "Detect Isolated Vertices"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        global isolated_vertex_count
        obj = context.active_object

        if not obj or obj.type != 'MESH':
            self.report({'WARNING'}, "请选择一个网格对象。")
            return {'CANCELLED'}

        # 执行检测
        isolated_indices = detect_isolated_vertices_logic(obj)
        isolated_vertex_count = len(isolated_indices)

        if isolated_vertex_count > 0:
            # 执行高亮
            highlight_isolated_vertices_logic(obj, isolated_indices)
            self.report({'INFO'}, f"检测到 {isolated_vertex_count} 个孤立顶点")
        else:
            self.report({'INFO'}, "未检测到孤立顶点")

        return {'FINISHED'}
