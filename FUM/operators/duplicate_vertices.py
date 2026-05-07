import bpy
import bmesh
from mathutils import kdtree

# 全局变量，用于存储重复顶点的数量，以便在UI中显示
duplicate_vertex_count = 0

def detect_duplicate_vertices_logic(obj, threshold=0.0001):
    """
    检测 Blender mesh 对象中距离小于给定阈值的重复顶点。
    使用 KDTree 空间索引优化，适用于高面数模型。

    Args:
        obj (bpy.types.Object): 当前选中的 mesh 对象。
        threshold (float): 距离阈值。

    Returns:
        list: 包含重复顶点索引的列表。
    """
    duplicate_indices = set()

    # 确保对象是网格类型
    if not obj or obj.type != 'MESH':
        return []

    # 获取网格数据并创建 BMesh
    mesh = obj.data
    bm = bmesh.new()
    bm.from_mesh(mesh)
    bm.verts.ensure_lookup_table()

    # 构建 KDTree 以高效查找近邻顶点 (O(N log N))
    size = len(bm.verts)
    kd = kdtree.KDTree(size)

    for i, v in enumerate(bm.verts):
        kd.insert(v.co, i)

    kd.balance()

    # 遍历所有顶点，查找重复项
    for i, v in enumerate(bm.verts):
        # 查找距离当前顶点小于阈值的所有顶点
        # query_radius 返回 (坐标, 索引, 距离) 的列表
        for (co, index, dist) in kd.find_range(v.co, threshold):
            # 排除自身索引
            if index != i:
                duplicate_indices.add(i)

    # 释放 BMesh 资源
    bm.free()

    return list(duplicate_indices)


class FUM_OT_DetectDuplicateVertices(bpy.types.Operator):
    """检测并高亮显示模型中的重复顶点"""
    bl_idname = "fum.detect_duplicate_vertices"
    bl_label = "检测重复顶点"
    bl_options = {'REGISTER', 'UNDO'}

    threshold: bpy.props.FloatProperty(
        name="阈值",
        description="距离阈值，小于此距离的顶点被视为重复",
        default=0.0001,
        min=0.000001,
        max=1.0,
        step=3,
        precision=6,
    )

    def execute(self, context):
        global duplicate_vertex_count
        duplicate_vertex_count = 0 # 重置计数

        obj = context.active_object

        if not obj or obj.type != 'MESH':
            self.report({'WARNING'}, "请选择一个网格对象。")
            return {'CANCELLED'}

        original_mode = obj.mode

        if obj.mode != 'EDIT':
            bpy.ops.object.mode_set(mode='EDIT')

        # 调用核心检测逻辑
        duplicate_verts = detect_duplicate_vertices_logic(obj, self.threshold)
        duplicate_vertex_count = len(duplicate_verts)

        # 高亮显示重复顶点
        bm = bmesh.from_edit_mesh(obj.data)
        bm.verts.ensure_lookup_table()

        # 清除当前选择
        for elem in (*bm.verts, *bm.edges, *bm.faces):
            elem.select = False

        for vert_idx in duplicate_verts:
            if vert_idx < len(bm.verts):
                bm.verts[vert_idx].select = True

        bmesh.update_edit_mesh(obj.data)

        # 恢复模式
        bpy.ops.object.mode_set(mode=original_mode)

        # 在控制台输出详细信息
        print("\n--- FUM 重复顶点检测结果 ---")
        print(f"检测到 {duplicate_vertex_count} 个重复顶点。")
        if duplicate_vertex_count > 0:
            print(f"重复顶点索引: {duplicate_verts}")
        print("---------------------------")

        # 在UI中报告结果
        if duplicate_vertex_count > 0:
            self.report({'INFO'}, f"检测到 {duplicate_vertex_count} 个重复顶点，已高亮显示。")
        else:
            self.report({'INFO'}, "未检测到重复顶点。")

        return {'FINISHED'}
