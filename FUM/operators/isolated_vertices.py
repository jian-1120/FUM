import bpy
import bmesh

class FUM_OT_DetectIsolatedVertices(bpy.types.Operator):
    """检测并高亮显示模型中的孤立顶点"""
    bl_idname = "fum.detect_isolated_vertices"
    bl_label = "检测孤立顶点"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def execute(self, context):
        obj = context.active_object
        original_mode = obj.mode
        original_select_mode = context.tool_settings.mesh_select_mode[:]
        
        try:
            if obj.mode != 'EDIT':
                bpy.ops.object.mode_set(mode='EDIT')

            context.tool_settings.mesh_select_mode = (True, False, False)
            bm = bmesh.from_edit_mesh(obj.data)
            bm.verts.ensure_lookup_table()

            # 清除当前所有选择
            for elem in (*bm.verts, *bm.edges, *bm.faces):
                elem.select = False

            isolated_indices = [v.index for v in bm.verts if len(v.link_edges) == 0]
            
            for idx in isolated_indices:
                bm.verts[idx].select = True

            context.scene.fum_isolated_vertex_count = len(isolated_indices)
            bmesh.update_edit_mesh(obj.data)

            if context.scene.fum_isolated_vertex_count > 0:
                self.report({'INFO'}, f"检测到 {context.scene.fum_isolated_vertex_count} 个孤立顶点，已高亮显示。")
            else:
                self.report({'INFO'}, "未检测到孤立顶点。")

        except Exception as e:
            self.report({"ERROR"}, f"检测失败: {str(e)}")
            return {"CANCELLED"}
        finally:
            if obj.mode != original_mode:
                bpy.ops.object.mode_set(mode=original_mode)
            context.tool_settings.mesh_select_mode = original_select_mode

        return {'FINISHED'}
