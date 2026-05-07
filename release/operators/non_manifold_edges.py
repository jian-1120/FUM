import bpy
import bmesh

# 全局变量，用于存储非流形边的数量，以便在UI中显示
non_manifold_edge_count = 0

class FUM_OT_DetectNonManifoldEdges(bpy.types.Operator):
    """检测并高亮显示模型中的非流形边"""
    bl_idname = "fum.detect_non_manifold_edges"
    bl_label = "检测非流形边"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        global non_manifold_edge_count
        non_manifold_edge_count = 0 # 重置计数

        obj = context.active_object

        if not obj or obj.type != 'MESH':
            self.report({"WARNING"}, "请选择一个网格对象。")
            return {"CANCELLED"}

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
        print("\n--- FUM 非流形边检测结果 ---")
        print(f"检测到 {non_manifold_edge_count} 条非流形边。")
        if non_manifold_edge_count > 0:
            print("非流形边索引：")
            for edge in non_manifold_edges:
                print(f"  Edge Index: {edge.index}")
        print("---------------------------")

        # 在UI中报告结果
        if non_manifold_edge_count > 0:
            self.report({"INFO"}, f"检测到 {non_manifold_edge_count} 条非流形边，已高亮显示。")
        else:
            self.report({"INFO"}, "未检测到非流形边。")

        return {"FINISHED"}
