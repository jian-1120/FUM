import bpy


class VIEW3D_PT_FUMPanel(bpy.types.Panel):
    """FUM plugin main panel."""

    bl_label = "FUM"
    bl_idname = "VIEW3D_PT_FUMPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "FUM"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        preflight_box = layout.box()
        preflight_box.label(text="Export Preflight", icon="EXPORT")

        action_column = preflight_box.column(align=True)
        action_column.scale_y = 1.2
        action_column.operator("fum.export_preflight_check", text="Run Export Check", icon="PLAY")

        status = scene.fum_preflight_status
        if status != "NONE":
            status_box = preflight_box.box()
            if status == "PASS":
                status_box.label(text="RESULT: PASS", icon="CHECKMARK")
                status_box.label(text="Mesh is ready for export.")
            elif status == "WARNING":
                status_box.label(text="RESULT: WARNING", icon="ERROR")
                status_box.label(text="Review non-blocking issues before export.")
            elif status == "FAIL":
                status_box.label(text="RESULT: FAIL", icon="CANCEL")
                status_box.label(text="Blocking export issues were detected.")

            status_box.label(text=f"Total Issues: {scene.fum_preflight_total_issues}")
            summary = scene.fum_preflight_summary
            if summary:
                status_box.label(text=summary[:120])

        counts_box = preflight_box.box()
        counts_box.label(text="Inspection Summary", icon="INFO")
        counts_box.label(text=f"Non-manifold Edges: {scene.fum_non_manifold_count}")
        counts_box.label(text=f"Duplicate Vertices: {scene.fum_duplicate_vertex_count}")
        counts_box.label(text=f"Flipped Normals: {scene.fum_flipped_normal_count}")
        counts_box.label(text=f"N-Gons: {scene.fum_ngon_count}")
        counts_box.label(text=f"Isolated Vertices: {scene.fum_isolated_vertex_count}")

        layout.separator()
        layout.label(text="Individual Inspection Tools", icon="TOOL_SETTINGS")

        column = layout.column(align=True)
        column.operator("fum.full_inspection", text="Run Full Inspection", icon="VIEWZOOM")
        layout.separator()

        box = layout.box()
        box.label(text="非流形边检测", icon="MESH_DATA")
        row = box.row()
        row.operator("fum.detect_non_manifold_edges", text="开始检测")
        row = box.row()
        if scene.fum_non_manifold_count > 0:
            row.label(text=f"检测到 {scene.fum_non_manifold_count} 条问题边", icon="ERROR")
        else:
            row.label(text="未检测到非流形边", icon="CHECKMARK")

        box = layout.box()
        box.label(text="重复顶点检测", icon="VERTEXSEL")
        row = box.row()
        detect_duplicates_op = row.operator("fum.detect_duplicate_vertices", text="开始检测")
        row.prop(detect_duplicates_op, "threshold", text="阈值")
        row = box.row()
        if scene.fum_duplicate_vertex_count > 0:
            row.label(text=f"检测到 {scene.fum_duplicate_vertex_count} 个重复顶点", icon="ERROR")
        else:
            row.label(text="未检测到重复顶点", icon="CHECKMARK")

        box = layout.box()
        box.label(text="翻转法线检测", icon="FACESEL")
        row = box.row()
        row.operator("fum.detect_flipped_normals", text="开始检测")
        row = box.row()
        if scene.fum_flipped_normal_count > 0:
            row.label(text=f"检测到 {scene.fum_flipped_normal_count} 个翻转法线面", icon="ERROR")
        else:
            row.label(text="未检测到翻转法线面", icon="CHECKMARK")

        box = layout.box()
        box.label(text="N-Gon 检测", icon="MESH_ICOSPHERE")
        row = box.row()
        row.operator("fum.detect_ngons", text="开始检测")
        row = box.row()
        if scene.fum_ngon_count > 0:
            row.label(text=f"检测到 {scene.fum_ngon_count} 个 N-Gons", icon="ERROR")
        else:
            row.label(text="未检测到 N-Gons", icon="CHECKMARK")

        box = layout.box()
        box.label(text="孤立顶点检测", icon="DOT")
        row = box.row()
        row.operator("fum.detect_isolated_vertices", text="开始检测")
        row = box.row()
        if scene.fum_isolated_vertex_count > 0:
            row.label(text=f"检测到 {scene.fum_isolated_vertex_count} 个孤立顶点", icon="ERROR")
        else:
            row.label(text="未检测到孤立顶点", icon="CHECKMARK")
