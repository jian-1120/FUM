import bpy


class FUM_OT_FullInspection(bpy.types.Operator):
    """Run the complete FUM inspection workflow."""

    bl_idname = "fum.full_inspection"
    bl_label = "Run Full Inspection"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == "MESH"

    def execute(self, context):
        result = bpy.ops.fum.export_preflight_check()
        if "FINISHED" in result:
            status = context.scene.fum_preflight_status
            total_issues = context.scene.fum_preflight_total_issues
            self.report({"INFO"}, f"Full inspection complete: {status} ({total_issues} issues found).")
        return result
