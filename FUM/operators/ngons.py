import bpy
import bmesh

class FUM_OT_DetectNGons(bpy.types.Operator):
    """检测并高亮显示模型中的 N-Gons（边数 > 4 的面）"""
    bl_idname = "fum.detect_ngons"
    bl_label = "检测 N-Gons"
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

            context.tool_settings.mesh_select_mode = (False, False, True)
            bm = bmesh.from_edit_mesh(obj.data)
            bm.faces.ensure_lookup_table()

            # 清除当前所有选择
            for elem in (*bm.verts, *bm.edges, *bm.faces):
                elem.select = False

            ngon_indices = [f.index for f in bm.faces if len(f.verts) > 4]
            
            for idx in ngon_indices:
                bm.faces[idx].select = True

            context.scene.fum_ngon_count = len(ngon_indices)
            bmesh.update_edit_mesh(obj.data)

            if context.scene.fum_ngon_count > 0:
                self.report({'INFO'}, f"检测到 {context.scene.fum_ngon_count} 个 N-Gons，已高亮显示。")
            else:
                self.report({'INFO'}, "未检测到 N-Gons。")

        except Exception as e:
            self.report({"ERROR"}, f"检测失败: {str(e)}")
            return {"CANCELLED"}
        finally:
            if obj.mode != original_mode:
                bpy.ops.object.mode_set(mode=original_mode)
            context.tool_settings.mesh_select_mode = original_select_mode

        return {'FINISHED'}
