import bpy

class FUM_OT_FullInspection(bpy.types.Operator):
    """运行所有检测系统并汇总结果"""
    bl_idname = "fum.full_inspection"
    bl_label = "一键全检"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def execute(self, context):
        # 按顺序运行所有检测操作器
        # 注意：每个操作器都会高亮自己的结果，最后一个运行的会覆盖之前的选择
        # 但计数会保留在 Scene 属性中
        
        bpy.ops.fum.detect_non_manifold_edges()
        bpy.ops.fum.detect_duplicate_vertices()
        bpy.ops.fum.detect_flipped_normals()
        bpy.ops.fum.detect_ngons()
        bpy.ops.fum.detect_isolated_vertices()
        
        s = context.scene
        total_issues = (
            s.fum_non_manifold_count +
            s.fum_duplicate_vertex_count +
            s.fum_flipped_normal_count +
            s.fum_ngon_count +
            s.fum_isolated_vertex_count
        )
        
        self.report({'INFO'}, f"全检完成！共发现 {total_issues} 个潜在问题。")
        
        return {'FINISHED'}
