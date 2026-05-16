import bpy
import bmesh


class FUM_OT_DetectFlippedNormals(bpy.types.Operator):
    """Detect and highlight faces whose normals appear flipped."""

    bl_idname = "fum.detect_flipped_normals"
    bl_label = "Detect Flipped Normals"
    bl_description = "Find faces whose normals differ from recalculated outward normals"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == "MESH"

    def execute(self, context):
        obj = context.active_object
        original_mode = obj.mode
        original_select_mode = tuple(context.tool_settings.mesh_select_mode)

        bm_original = None
        bm_recalculated = None

        try:
            mesh = obj.data
            bm_recalculated = bmesh.new()
            bm_recalculated.from_mesh(mesh)
            bm_recalculated.faces.ensure_lookup_table()
            bmesh.ops.recalc_face_normals(bm_recalculated, faces=bm_recalculated.faces)

            flipped_indices = []
            bm_original = bmesh.new()
            bm_original.from_mesh(mesh)
            bm_original.faces.ensure_lookup_table()

            for index, original_face in enumerate(bm_original.faces):
                if original_face.normal.dot(bm_recalculated.faces[index].normal) < -0.999:
                    flipped_indices.append(index)

            if obj.mode != "EDIT":
                bpy.ops.object.mode_set(mode="EDIT")

            context.tool_settings.mesh_select_mode = (False, False, True)
            bm = bmesh.from_edit_mesh(obj.data)
            bm.faces.ensure_lookup_table()

            for elem in (*bm.verts, *bm.edges, *bm.faces):
                elem.select = False

            for index in flipped_indices:
                bm.faces[index].select = True

            context.scene.fum_flipped_normal_count = len(flipped_indices)
            bmesh.update_edit_mesh(obj.data)

            if context.scene.fum_flipped_normal_count > 0:
                self.report({"ERROR"}, f"{context.scene.fum_flipped_normal_count} flipped normals detected.")
            else:
                self.report({"INFO"}, "No issues detected.")

        except Exception as error:
            self.report({"ERROR"}, f"Flipped normal detection failed: {str(error)}")
            return {"CANCELLED"}
        finally:
            if bm_original is not None:
                bm_original.free()
            if bm_recalculated is not None:
                bm_recalculated.free()
            if obj.mode != original_mode:
                bpy.ops.object.mode_set(mode=original_mode)
            context.tool_settings.mesh_select_mode = original_select_mode

        return {"FINISHED"}
