import bpy
import bmesh


class FUM_OT_DetectIsolatedVertices(bpy.types.Operator):
    """Detect and highlight vertices with no connected edges."""

    bl_idname = "fum.detect_isolated_vertices"
    bl_label = "Detect Isolated Vertices"
    bl_description = "Find vertices with no connected edges and highlight them in Edit Mode"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == "MESH"

    def execute(self, context):
        obj = context.active_object
        original_mode = obj.mode
        original_select_mode = context.tool_settings.mesh_select_mode[:]

        try:
            if obj.mode != "EDIT":
                bpy.ops.object.mode_set(mode="EDIT")

            # Force correct selection mode for visibility
            context.tool_settings.mesh_select_mode = (True, False, False)
            
            bm = bmesh.from_edit_mesh(obj.data)
            bm.verts.ensure_lookup_table()

            for elem in (*bm.verts, *bm.edges, *bm.faces):
                elem.select = False

            isolated_indices = [vertex.index for vertex in bm.verts if len(vertex.link_edges) == 0]
            for index in isolated_indices:
                bm.verts[index].select = True

            context.scene.fum_isolated_vertex_count = len(isolated_indices)
            bmesh.update_edit_mesh(obj.data)

            # Force viewport refresh
            for area in context.screen.areas:
                if area.type == 'VIEW_3D':
                    area.tag_redraw()

            if context.scene.fum_isolated_vertex_count > 0:
                self.report({"WARNING"}, f"{context.scene.fum_isolated_vertex_count} isolated vertices detected.")
            else:
                self.report({"INFO"}, "No issues detected.")

        except Exception as error:
            self.report({"ERROR"}, f"Isolated vertex detection failed: {str(error)}")
            return {"CANCELLED"}
        finally:
            # Restore original selection mode
            context.tool_settings.mesh_select_mode = original_select_mode
            
            if obj.mode != original_mode:
                bpy.ops.object.mode_set(mode=original_mode)

        return {"FINISHED"}
