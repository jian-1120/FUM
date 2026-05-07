import bpy

from ..operators.non_manifold_edges import non_manifold_edge_count
from ..operators.duplicate_vertices import duplicate_vertex_count

class VIEW3D_PT_FUMPanel(bpy.types.Panel):
    """FUM 插件主面板"""
    bl_label = "FUM"
    bl_idname = "VIEW3D_PT_FUMPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'FUM'

    def draw(self, context):
        layout = self.layout

        # 非流形边检测部分
        box = layout.box()
        box.label(text="非流形边检测")
        row = box.row()
        row.operator("fum.detect_non_manifold_edges")
        row = box.row()
        if non_manifold_edge_count > 0:
            row.label(text=f"检测到 {non_manifold_edge_count} 条问题边")
        else:
            row.label(text="未检测到非流形边")

        # 重复顶点检测部分
        box = layout.box()
        box.label(text="重复顶点检测")
        row = box.row()
        # 增加一个属性行来显示和修改阈值
        detect_duplicates_op = row.operator("fum.detect_duplicate_vertices")
        row.prop(detect_duplicates_op, "threshold", text="阈值")
        row = box.row()
        if duplicate_vertex_count > 0:
            row.label(text=f"检测到 {duplicate_vertex_count} 个重复顶点")
        else:
            row.label(text="未检测到重复顶点")
