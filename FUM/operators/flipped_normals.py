import bpy
import bmesh

class FUM_OT_DetectFlippedNormals(bpy.types.Operator):
    """检测并高亮显示模型中的翻转法线面"""
    bl_idname = "fum.detect_flipped_normals"
    bl_label = "检测翻转法线"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def execute(self, context):
        obj = context.active_object
        original_mode = obj.mode
        original_select_mode = context.tool_settings.mesh_select_mode[:]
        
        try:
            # 1. 检测逻辑 (在副本上进行以避免修改原始数据)
            mesh = obj.data
            bm_recalc = bmesh.new()
            bm_recalc.from_mesh(mesh)
            bm_recalc.faces.ensure_lookup_table()
            
            # 执行向外重计算法线
            bmesh.ops.recalc_face_normals(bm_recalc, faces=bm_recalc.faces)
            
            # 找出翻转的面索引
            flipped_indices = []
            bm_orig = bmesh.new()
            bm_orig.from_mesh(mesh)
            bm_orig.faces.ensure_lookup_table()
            
            for i, face_orig in enumerate(bm_orig.faces):
                if face_orig.normal.dot(bm_recalc.faces[i].normal) < -0.999:
                    flipped_indices.append(i)
            
            bm_orig.free()
            bm_recalc.free()
            
            # 2. 高亮逻辑
            if obj.mode != 'EDIT':
                bpy.ops.object.mode_set(mode='EDIT')
            
            context.tool_settings.mesh_select_mode = (False, False, True)
            bm = bmesh.from_edit_mesh(obj.data)
            bm.faces.ensure_lookup_table()
            
            for elem in (*bm.verts, *bm.edges, *bm.faces):
                elem.select = False
                
            for idx in flipped_indices:
                bm.faces[idx].select = True
                
            context.scene.fum_flipped_normal_count = len(flipped_indices)
            bmesh.update_edit_mesh(obj.data)

            if context.scene.fum_flipped_normal_count > 0:
                self.report({'INFO'}, f"检测到 {context.scene.fum_flipped_normal_count} 个翻转法线面，已高亮显示。")
            else:
                self.report({'INFO'}, "未检测到翻转法线面。")

        except Exception as e:
            self.report({"ERROR"}, f"检测失败: {str(e)}")
            return {"CANCELLED"}
        finally:
            if obj.mode != original_mode:
                bpy.ops.object.mode_set(mode=original_mode)
            context.tool_settings.mesh_select_mode = original_select_mode

        return {'FINISHED'}
