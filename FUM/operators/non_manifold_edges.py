import bpy
import bmesh


class FUM_OT_DetectNonManifoldEdges(bpy.types.Operator):
    """Detect and highlight non-manifold edges in the active mesh."""

    bl_idname = "fum.detect_non_manifold_edges"
    bl_label = "Detect Non-Manifold Edges"
    bl_description = "Find non-manifold edges and highlight them in Edit Mode"
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

            context.tool_settings.mesh_select_mode = (False, True, False)
            bm = bmesh.from_edit_mesh(obj.data)

            for elem in (*bm.verts, *bm.edges, *bm.faces):
                elem.select = False

            non_manifold_edges = [edge for edge in bm.edges if not edge.is_manifold]
            for edge in non_manifold_edges:
                edge.select = True

            # Set highlight color to bright red for better visibility
            context.preferences.themes[0].view_3d.edge_select = (1.0, 0.15, 0.15)

            context.scene.fum_non_manifold_count = len(non_manifold_edges)
            bmesh.update_edit_mesh(obj.data)

            if context.scene.fum_non_manifold_count > 0:
                self.report({"WARNING"}, f"{context.scene.fum_non_manifold_count} non-manifold edges detected.")
            else:
                self.report({"INFO"}, "No issues detected.")

        except Exception as error:
            self.report({"ERROR"}, f"Non-manifold edge detection failed: {str(error)}")
            return {"CANCELLED"}
        finally:
            if obj.mode != "EDIT":
                bpy.ops.object.mode_set(mode="EDIT")
            context.tool_settings.mesh_select_mode = original_select_mode
            if obj.mode != original_mode:
                bpy.ops.object.mode_set(mode=original_mode)

        return {"FINISHED"}
