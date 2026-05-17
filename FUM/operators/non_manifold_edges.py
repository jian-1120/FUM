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
        
        # Save original theme color
        theme = context.preferences.themes[0].view_3d
        original_edge_select = tuple(theme.edge_select)

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

            # Set highlight color to magenta for maximum visibility
            theme.edge_select = (1.0, 0.1, 0.6)

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
            # Restore original theme color
            theme.edge_select = original_edge_select
            
            if obj.mode != "EDIT":
                bpy.ops.object.mode_set(mode="EDIT")
            context.tool_settings.mesh_select_mode = original_select_mode
            if obj.mode != original_mode:
                bpy.ops.object.mode_set(mode=original_mode)

        return {"FINISHED"}
