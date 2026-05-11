import bpy
import bmesh
from mathutils import kdtree

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
            bm.verts.ensure_lookup_table()

            # 清除当前选择
            for elem in (*bm.verts, *bm.edges, *bm.faces):
                elem.select = False

            # 构建 KDTree 以高效查找近邻顶点 (O(N log N))
            size = len(bm.verts)
            kd = kdtree.KDTree(size)
            for i, v in enumerate(bm.verts):
                kd.insert(v.co, i)
            kd.balance()

            duplicate_indices = set()
            for i, v in enumerate(bm.verts):
                for (co, index, dist) in kd.find_range(v.co, self.threshold):
                    if index != i:
                        duplicate_indices.add(i)

            for vert_idx in duplicate_indices:
                bm.verts[vert_idx].select = True

            context.scene.fum_duplicate_vertex_count = len(duplicate_indices)
            bmesh.update_edit_mesh(obj.data)

            if context.scene.fum_duplicate_vertex_count > 0:
                self.report({'INFO'}, f"检测到 {context.scene.fum_duplicate_vertex_count} 个重复顶点，已高亮显示。")
            else:
                self.report({'INFO'}, "未检测到重复顶点。")

        except Exception as e:
            self.report({"ERROR"}, f"检测失败: {str(e)}")
            return {"CANCELLED"}
        finally:
            if obj.mode != original_mode:
                bpy.ops.object.mode_set(mode=original_mode)

        return {'FINISHED'}
