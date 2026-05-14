import bpy


CHECKS = (
    {
        "label": "Non-manifold Edges",
        "operator": "fum.detect_non_manifold_edges",
        "scene_property": "fum_non_manifold_count",
        "severity": "FAIL",
    },
    {
        "label": "Duplicate Vertices",
        "operator": "fum.detect_duplicate_vertices",
        "scene_property": "fum_duplicate_vertex_count",
        "severity": "WARNING",
    },
    {
        "label": "Flipped Normals",
        "operator": "fum.detect_flipped_normals",
        "scene_property": "fum_flipped_normal_count",
        "severity": "FAIL",
    },
    {
        "label": "N-Gons",
        "operator": "fum.detect_ngons",
        "scene_property": "fum_ngon_count",
        "severity": "WARNING",
    },
    {
        "label": "Isolated Vertices",
        "operator": "fum.detect_isolated_vertices",
        "scene_property": "fum_isolated_vertex_count",
        "severity": "WARNING",
    },
)


def build_preflight_summary(scene):
    """Return a stable export-readiness summary from Scene inspection counters."""
    issue_counts = {
        check["label"]: int(getattr(scene, check["scene_property"], 0))
        for check in CHECKS
    }
    total_issues = sum(issue_counts.values())
    blocking_issues = sum(
        issue_counts[check["label"]]
        for check in CHECKS
        if check["severity"] == "FAIL"
    )

    if total_issues == 0:
        status = "PASS"
        report_type = {"INFO"}
        headline = "Mesh is ready for export."
    elif blocking_issues > 0:
        status = "FAIL"
        report_type = {"ERROR"}
        headline = "Blocking export issues were detected."
    else:
        status = "WARNING"
        report_type = {"WARNING"}
        headline = "Review non-blocking mesh issues before export."

    detail_parts = [f"{name}: {count}" for name, count in issue_counts.items()]
    detail = f"{headline} Total issues: {total_issues}. " + "; ".join(detail_parts)

    return status, report_type, total_issues, detail, issue_counts


class FUM_OT_ExportPreflightCheck(bpy.types.Operator):
    """Run every FUM mesh inspection and produce an export-readiness summary."""

    bl_idname = "fum.export_preflight_check"
    bl_label = "Run Export Preflight"
    bl_description = "Run all FUM mesh inspections and report export readiness"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == "MESH"

    def execute(self, context):
        scene = context.scene
        active_object = context.active_object
        original_mode = active_object.mode if active_object else "OBJECT"

        try:
            for check in CHECKS:
                operator = check["operator"]
                op_module, op_name = operator.split(".", 1)
                op_group = getattr(bpy.ops, op_module)
                op_callable = getattr(op_group, op_name)
                result = op_callable()
                if "CANCELLED" in result:
                    scene.fum_preflight_status = "FAIL"
                    scene.fum_preflight_total_issues = 0
                    scene.fum_preflight_summary = f"Export preflight cancelled while running {check['label']}."
                    self.report({"ERROR"}, scene.fum_preflight_summary)
                    return {"CANCELLED"}

            status, report_type, total_issues, detail, _issue_counts = build_preflight_summary(scene)
            scene.fum_preflight_status = status
            scene.fum_preflight_total_issues = total_issues
            scene.fum_preflight_summary = detail

            self.report(report_type, f"EXPORT PREFLIGHT: {status} ({total_issues} issues found)")
            return {"FINISHED"}
        finally:
            if active_object and active_object.mode != original_mode:
                try:
                    bpy.ops.object.mode_set(mode=original_mode)
                except RuntimeError:
                    bpy.ops.object.mode_set(mode="OBJECT")
            if active_object:
                context.view_layer.objects.active = active_object
