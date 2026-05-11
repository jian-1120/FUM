import bpy
import bmesh

class FUM_OT_DetectNonManifoldEdges(bpy.types.Operator):
    """检测并高亮显示模型中的非流形边"""
    bl_idname = "fum.detect_non_manifold_edges"
    bl_label = "检测非流形边"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def execute(self, context):
        obj = context.active_object
        original_mode = obj.mode
        
        try:
            if obj.mode != 'EDIT':
                bpy.ops.object.mode_set(mode='EDIT')

            bm = bmesh.from_edit_mesh(obj.data)

            # 清除选择
            for elem in (*bm.verts, *bm.edges, *bm.faces):
                elem.select = False

            non_manifold_edges = [e for e in bm.edges if not e.is_manifold]
            
            for edge in non_manifold_edges:
                edge.select = True

            # 更新计数到 Scene 属性
            context.scene.fum_non_manifold_count = len(non_manifold_edges)
            bmesh.update_edit_mesh(obj.data)

            if context.scene.fum_non_manifold_count > 0:
                self.report({"INFO"}, f"检测到 {context.scene.fum_non_manifold_count} 条非流形边，已高亮显示。")
            else:
                self.report({"INFO"}, "未检测到非流形边。")

        except Exception as e:
            self.report({"ERROR"}, f"检测失败: {str(e)}")
            return {"CANCELLED"}
        finally:
            if obj.mode != original_mode:
                bpy.ops.object.mode_set(mode=original_mode)

        return {"FINISHED"}
