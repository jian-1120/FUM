import bpy

class VIEW3D_PT_FUMPanel(bpy.types.Panel):
    """FUM 插件主面板"""
    bl_label = "FUM"
    bl_idname = "VIEW3D_PT_FUMPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'FUM'

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # --- Export Preflight Section ---
        box = layout.box()
        box.label(text="Export Preflight", icon='EXPORT')
        
        col = box.column(align=True)
        col.scale_y = 1.2
        col.operator("fum.export_preflight_check", text="Run Export Check", icon='PLAY')
        
        # Display Preflight Status
        status = scene.fum_preflight_status
        if status != "NONE":
            status_box = box.box()
            if status == "PASS":
                status_box.label(text="RESULT: PASS", icon='CHECKMARK')
                status_box.label(text="Mesh is ready for export.")
            elif status == "WARNING":
                status_box.label(text="RESULT: WARNING", icon='ERROR')
                status_box.label(text="Minor issues detected.")
            elif status == "FAIL":
                status_box.label(text="RESULT: FAIL", icon='CANCEL')
                status_box.label(text="Critical issues found!")
        
        layout.separator()

        # --- Individual Tools Section ---
        layout.label(text="Individual Inspection Tools", icon='TOOL_SETTINGS')
        
        # 一键全检按钮
        col = layout.column(align=True)
        col.operator("fum.full_inspection", icon='VIEWZOOM')
        layout.separator()

        # 非流形边检测部分
        box = layout.box()
        box.label(text="非流形边检测", icon='MESH_DATA')
        row = box.row()
        row.operator("fum.detect_non_manifold_edges", text="开始检测")
        row = box.row()
        if scene.fum_non_manifold_count > 0:
            row.label(text=f"检测到 {scene.fum_non_manifold_count} 条问题边", icon='ERROR')
        else:
            row.label(text="未检测到非流形边", icon='CHECKMARK')

        # 重复顶点检测部分
        box = layout.box()
        box.label(text="重复顶点检测", icon='VERTEXSEL')
        row = box.row()
        detect_duplicates_op = row.operator("fum.detect_duplicate_vertices", text="开始检测")
        row.prop(detect_duplicates_op, "threshold", text="阈值")
        row = box.row()
        if scene.fum_duplicate_vertex_count > 0:
            row.label(text=f"检测到 {scene.fum_duplicate_vertex_count} 个重复顶点", icon='ERROR')
        else:
            row.label(text="未检测到重复顶点", icon='CHECKMARK')

        # 翻转法线检测部分
        box = layout.box()
        box.label(text="翻转法线检测", icon='FACESEL')
        row = box.row()
        row.operator("fum.detect_flipped_normals", text="开始检测")
        row = box.row()
        if scene.fum_flipped_normal_count > 0:
            row.label(text=f"检测到 {scene.fum_flipped_normal_count} 个翻转法线面", icon='ERROR')
        else:
            row.label(text="未检测到翻转法线面", icon='CHECKMARK')

        # N-Gon 检测部分
        box = layout.box()
        box.label(text="N-Gon 检测", icon='MESH_ICOSPHERE')
        row = box.row()
        row.operator("fum.detect_ngons", text="开始检测")
        row = box.row()
        if scene.fum_ngon_count > 0:
            row.label(text=f"检测到 {scene.fum_ngon_count} 个 N-Gons", icon='ERROR')
        else:
            row.label(text="未检测到 N-Gons", icon='CHECKMARK')

        # 孤立顶点检测部分
        box = layout.box()
        box.label(text="孤立顶点检测", icon='DOT')
        row = box.row()
        row.operator("fum.detect_isolated_vertices", text="开始检测")
        row = box.row()
        if scene.fum_isolated_vertex_count > 0:
            row.label(text=f"检测到 {scene.fum_isolated_vertex_count} 个孤立顶点", icon='ERROR')
        else:
            row.label(text="未检测到孤立顶点", icon='CHECKMARK')
