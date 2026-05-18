import bpy
import bmesh
from mathutils import kdtree


class FUM_OT_DetectDuplicateVertices(bpy.types.Operator):
    """Detect and highlight duplicate vertices in the active mesh."""

    bl_idname = "fum.detect_duplicate_vertices"
    bl_label = "Detect Duplicate Vertices"
    bl_description = "Find vertices closer than the configured threshold and highlight them in Edit Mode"
    bl_options = {"REGISTER", "UNDO"}

    threshold: bpy.props.FloatProperty(
        name="Threshold",
        description="Distance threshold used to classify vertices as duplicates",
        default=0.0001,
        min=0.000001,
        max=1.0,
        step=3,
        precision=6,
    )

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

            duplicate_indices = set()
            vertex_count = len(bm.verts)
            if vertex_count > 0:
                kd = kdtree.KDTree(vertex_count)
                for index, vertex in enumerate(bm.verts):
                    kd.insert(vertex.co, index)
                kd.balance()

                for index, vertex in enumerate(bm.verts):
                    for _co, nearby_index, _dist in kd.find_range(vertex.co, self.threshold):
                        if nearby_index != index:
                            duplicate_indices.add(index)

            for vertex_index in duplicate_indices:
                bm.verts[vertex_index].select = True

            context.scene.fum_duplicate_vertex_count = len(duplicate_indices)
            bmesh.update_edit_mesh(obj.data)

            # Force viewport refresh
            for area in context.screen.areas:
                if area.type == 'VIEW_3D':
                    area.tag_redraw()

            if context.scene.fum_duplicate_vertex_count > 0:
                self.report({"WARNING"}, f"{context.scene.fum_duplicate_vertex_count} duplicate vertices detected.")
            else:
                self.report({"INFO"}, "No issues detected.")

        except Exception as error:
            self.report({"ERROR"}, f"Duplicate vertex detection failed: {str(error)}")
            return {"CANCELLED"}
        finally:
            # Restore original selection mode
            context.tool_settings.mesh_select_mode = original_select_mode
            
            if obj.mode != original_mode:
                bpy.ops.object.mode_set(mode=original_mode)

        return {"FINISHED"}
