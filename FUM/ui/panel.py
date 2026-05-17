import bpy


class VIEW3D_PT_FUMPanel(bpy.types.Panel):
    """Main FUM panel for mesh inspection and export preflight."""

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
        action_column.scale_y = 1.25
        action_column.operator("fum.export_preflight_check", text="Run Export Preflight", icon="PLAY")

        status = scene.fum_preflight_status
        if status != "NONE":
            status_box = preflight_box.box()
            status_box.label(text=f"Status: {status}", icon=self._status_icon(status))
            status_box.label(text=self._status_message(status))
            status_box.label(text=f"Total Issues: {scene.fum_preflight_total_issues}")

            summary = scene.fum_preflight_summary
            if summary:
                status_box.label(text=summary[:120])
        else:
            preflight_box.label(text="Run the preflight check before exporting.", icon="INFO")

        counts_box = preflight_box.box()
        counts_box.label(text="Inspection Summary", icon="INFO")
        counts_box.label(text=f"Non-Manifold Edges: {scene.fum_non_manifold_count}")
        counts_box.label(text=f"Duplicate Vertices: {scene.fum_duplicate_vertex_count}")
        counts_box.label(text=f"Flipped Normals: {scene.fum_flipped_normal_count}")
        counts_box.label(text=f"N-Gons: {scene.fum_ngon_count}")
        counts_box.label(text=f"Isolated Vertices: {scene.fum_isolated_vertex_count}")

        layout.separator()
        layout.label(text="Targeted Inspection Tools", icon="TOOL_SETTINGS")

        layout.separator()

        self._draw_check_box(
            layout,
            title="Non-Manifold Edges",
            icon="MESH_DATA",
            operator="fum.detect_non_manifold_edges",
            count=scene.fum_non_manifold_count,
            issue_label="non-manifold edges",
            clear_label="No non-manifold edges detected.",
        )
        self._draw_check_box(
            layout,
            title="Duplicate Vertices",
            icon="VERTEXSEL",
            operator="fum.detect_duplicate_vertices",
            count=scene.fum_duplicate_vertex_count,
            issue_label="duplicate vertices",
            clear_label="No duplicate vertices detected.",
            threshold=True,
        )
        self._draw_check_box(
            layout,
            title="Flipped Normals",
            icon="FACESEL",
            operator="fum.detect_flipped_normals",
            count=scene.fum_flipped_normal_count,
            issue_label="faces with flipped normals",
            clear_label="No flipped normals detected.",
        )
        self._draw_check_box(
            layout,
            title="N-Gons",
            icon="MESH_ICOSPHERE",
            operator="fum.detect_ngons",
            count=scene.fum_ngon_count,
            issue_label="N-Gons",
            clear_label="No N-Gons detected.",
        )
        self._draw_check_box(
            layout,
            title="Isolated Vertices",
            icon="DOT",
            operator="fum.detect_isolated_vertices",
            count=scene.fum_isolated_vertex_count,
            issue_label="isolated vertices",
            clear_label="No isolated vertices detected.",
        )

    @staticmethod
    def _status_icon(status):
        if status == "PASS":
            return "CHECKMARK"
        if status == "WARNING":
            return "ERROR"
        if status == "FAIL":
            return "CANCEL"
        return "INFO"

    @staticmethod
    def _status_message(status):
        if status == "PASS":
            return "Mesh is ready for export."
        if status == "WARNING":
            return "Review non-blocking issues before export."
        if status == "FAIL":
            return "Blocking export issues were detected."
        return "Preflight status has not been calculated."

    @staticmethod
    def _draw_check_box(layout, title, icon, operator, count, issue_label, clear_label, threshold=False):
        box = layout.box()
        box.label(text=title, icon=icon)
        row = box.row()
        op = row.operator(operator, text="Run Check")
        if threshold:
            row.prop(op, "threshold", text="Threshold")

        result_row = box.row()
        if count > 0:
            result_row.label(text=f"Detected {count} {issue_label}.", icon="ERROR")
        else:
            result_row.label(text=clear_label, icon="CHECKMARK")
