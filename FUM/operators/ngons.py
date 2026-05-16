import bpy
import bmesh


class FUM_OT_DetectNGons(bpy.types.Operator):
    """Detect and highlight faces with more than four vertices."""

    bl_idname = "fum.detect_ngons"
    bl_label = "Detect N-Gons"
    bl_description = "Find faces with more than four vertices and highlight them in Edit Mode"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == "MESH"

    def execute(self, context):
        obj = context.active_object
        original_mode = obj.mode
        original_select_mode = tuple(context.tool_settings.mesh_select_mode)

        try:
            if obj.mode != "EDIT":
                bpy.ops.object.mode_set(mode="EDIT")

            context.tool_settings.mesh_select_mode = (False, False, True)
            bm = bmesh.from_edit_mesh(obj.data)
            bm.faces.ensure_lookup_table()

            for elem in (*bm.verts, *bm.edges, *bm.faces):
                elem.select = False

            ngon_indices = [face.index for face in bm.faces if len(face.verts) > 4]
            for index in ngon_indices:
                bm.faces[index].select = True

            context.scene.fum_ngon_count = len(ngon_indices)
            bmesh.update_edit_mesh(obj.data)

            if context.scene.fum_ngon_count > 0:
                self.report({"WARNING"}, f"{context.scene.fum_ngon_count} N-Gons detected.")
            else:
                self.report({"INFO"}, "No issues detected.")

        except Exception as error:
            self.report({"ERROR"}, f"N-Gon detection failed: {str(error)}")
            return {"CANCELLED"}
        finally:
            if obj.mode != original_mode:
                bpy.ops.object.mode_set(mode=original_mode)
            context.tool_settings.mesh_select_mode = original_select_mode

        return {"FINISHED"}
