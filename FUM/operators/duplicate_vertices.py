import bpy
import bmesh
from mathutils import kdtree


class FUM_OT_DetectDuplicateVertices(bpy.types.Operator):
    """Detect and highlight duplicate vertices in the active mesh."""

    bl_idname = "fum.detect_duplicate_vertices"
    bl_label = "检测重复顶点"
    bl_options = {"REGISTER", "UNDO"}

    threshold: bpy.props.FloatProperty(
        name="阈值",
        description="距离阈值，小于此距离的顶点被视为重复",
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
        original_select_mode = tuple(context.tool_settings.mesh_select_mode)

        try:
            if obj.mode != "EDIT":
                bpy.ops.object.mode_set(mode="EDIT")

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

            if context.scene.fum_duplicate_vertex_count > 0:
                self.report({"INFO"}, f"检测到 {context.scene.fum_duplicate_vertex_count} 个重复顶点，已高亮显示。")
            else:
                self.report({"INFO"}, "未检测到重复顶点。")

        except Exception as error:
            self.report({"ERROR"}, f"检测失败: {str(error)}")
            return {"CANCELLED"}
        finally:
            if obj.mode != "EDIT":
                bpy.ops.object.mode_set(mode="EDIT")
            context.tool_settings.mesh_select_mode = original_select_mode
            if obj.mode != original_mode:
                bpy.ops.object.mode_set(mode=original_mode)

        return {"FINISHED"}
