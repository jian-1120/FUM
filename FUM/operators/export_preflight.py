import bpy

class FUM_OT_ExportPreflightCheck(bpy.types.Operator):
    """运行导出预检并生成质量报告"""
    bl_idname = "fum.export_preflight_check"
    bl_label = "Run Export Check"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def execute(self, context):
        scene = context.scene
        
        # 运行所有检测系统
        bpy.ops.fum.detect_non_manifold_edges()
        bpy.ops.fum.detect_duplicate_vertices()
        bpy.ops.fum.detect_flipped_normals()
        bpy.ops.fum.detect_ngons()
        bpy.ops.fum.detect_isolated_vertices()
        
        # 汇总结果
        issues = {
            "Non-manifold Edges": scene.fum_non_manifold_count,
            "Duplicate Vertices": scene.fum_duplicate_vertex_count,
            "Flipped Normals": scene.fum_flipped_normal_count,
            "N-Gons": scene.fum_ngon_count,
            "Isolated Vertices": scene.fum_isolated_vertex_count
        }
        
        total_issues = sum(issues.values())
        
        # 判定状态
        if total_issues == 0:
            status = "PASS"
            report_type = {'INFO'}
        elif issues["Non-manifold Edges"] > 0 or issues["Flipped Normals"] > 0:
            # 严重问题判定为 FAIL
            status = "FAIL"
            report_type = {'ERROR'}
        else:
            # 只有 N-Gons 或重复顶点等判定为 WARNING
            status = "WARNING"
            report_type = {'WARNING'}
            
        # 存储状态到场景属性（稍后在 __init__.py 中定义）
        scene.fum_preflight_status = status
        
        # 生成报告
        self.report(report_type, f"EXPORT PREFLIGHT: {status} ({total_issues} issues found)")
        
        return {'FINISHED'}
