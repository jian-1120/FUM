
import bpy
import bmesh

bl_info = {
    "name": "FUM",
    "author": "Jian",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "3D Viewport > Sidebar > Model Doctor",
    "description": "Detects and highlights non-manifold edges in a mesh object.",
    "warning": "",
    "doc_url": "",
    "category": "Mesh",
}

# 全局变量，用于存储非流形边的数量，以便在UI中显示
non_manifold_edge_count = 0

class MODELDOCTOR_OT_DetectNonManifoldEdges(bpy.types.Operator):
    """检测并高亮显示模型中的非流形边"""
    bl_idname = "model_doctor.detect_non_manifold_edges"
    bl_label = "检测非流形边"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        global non_manifold_edge_count
        non_manifold_edge_count = 0 # 重置计数

        obj = context.active_object

        if not obj or obj.type != 'MESH':
            self.report({'WARNING'}, "请选择一个网格对象。")
            return {'CANCELLED'}

        original_mode = obj.mode

        if obj.mode != 'EDIT':
            bpy.ops.object.mode_set(mode='EDIT')

        bm = bmesh.from_edit_mesh(obj.data)

        # 清除选择
        for elem in (*bm.verts, *bm.edges, *bm.faces):
            elem.select = False

        non_manifold_edges = []

        for edge in bm.edges:
            if not edge.is_manifold:
                edge.select = True
                non_manifold_edges.append(edge)

        non_manifold_edge_count = len(non_manifold_edges)

        bmesh.update_edit_mesh(obj.data)

        # 恢复模式
        bpy.ops.object.mode_set(mode=original_mode)

        # 在控制台输出详细信息
        print("\n--- Model Doctor 检测结果 ---")
        print(f"检测到 {non_manifold_edge_count} 条非流形边。")
        if non_manifold_edge_count > 0:
            print("非流形边索引：")
            for edge in non_manifold_edges:
                print(f"  Edge Index: {edge.index}")
        print("---------------------------")

        # 在UI中报告结果
        if non_manifold_edge_count > 0:
            self.report({'INFO'}, f"检测到 {non_manifold_edge_count} 条非流形边，已高亮显示。")
        else:
            self.report({'INFO'}, "未检测到非流形边。")

        return {'FINISHED'}


class VIEW3D_PT_ModelDoctor(bpy.types.Panel):
    """在3D视图侧边栏创建Model Doctor面板"""
    bl_label = "FUM"
    bl_idname = "VIEW3D_PT_ModelDoctor"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'FUM'

    def draw(self, context):
        layout = self.layout

        # 添加检测按钮
        row = layout.row()
        row.operator(MODELDOCTOR_OT_DetectNonManifoldEdges.bl_idname)

        # 显示检测结果
        row = layout.row()
        if non_manifold_edge_count > 0:
            row.label(text=f"检测到 {non_manifold_edge_count} 条问题边")
        else:
            row.label(text="未检测到非流形边")


# 注册和注销函数
classes = (
    MODELDOCTOR_OT_DetectNonManifoldEdges,
    VIEW3D_PT_ModelDoctor,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
