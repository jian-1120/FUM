import bpy

from .operators.non_manifold_edges import FUM_OT_DetectNonManifoldEdges
from .operators.duplicate_vertices import FUM_OT_DetectDuplicateVertices
from .operators.flipped_normals import FUM_OT_DetectFlippedNormals
from .operators.ngons import FUM_OT_DetectNGons
from .operators.isolated_vertices import FUM_OT_DetectIsolatedVertices
from .operators.full_inspection import FUM_OT_FullInspection
from .operators.export_preflight import FUM_OT_ExportPreflightCheck
from .ui.panel import VIEW3D_PT_FUMPanel

bl_info = {
    "name": "FUM",
    "author": "Jian",
    "version": (1, 6),
    "blender": (4, 0, 0),
    "location": "3D Viewport > Sidebar > FUM",
    "description": "Export preflight and mesh inspection tools for Blender.",
    "warning": "",
    "doc_url": "https://github.com/jian-1120/FUM",
    "category": "Mesh",
}

classes = (
    FUM_OT_DetectNonManifoldEdges,
    FUM_OT_DetectDuplicateVertices,
    FUM_OT_DetectFlippedNormals,
    FUM_OT_DetectNGons,
    FUM_OT_DetectIsolatedVertices,
    FUM_OT_FullInspection,
    FUM_OT_ExportPreflightCheck,
    VIEW3D_PT_FUMPanel,
)

_SCENE_PROPERTIES = (
    "fum_non_manifold_count",
    "fum_duplicate_vertex_count",
    "fum_flipped_normal_count",
    "fum_ngon_count",
    "fum_isolated_vertex_count",
    "fum_preflight_status",
    "fum_preflight_total_issues",
    "fum_preflight_summary",
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.fum_non_manifold_count = bpy.props.IntProperty(name="Non-Manifold Count", default=0)
    bpy.types.Scene.fum_duplicate_vertex_count = bpy.props.IntProperty(name="Duplicate Vertex Count", default=0)
    bpy.types.Scene.fum_flipped_normal_count = bpy.props.IntProperty(name="Flipped Normal Count", default=0)
    bpy.types.Scene.fum_ngon_count = bpy.props.IntProperty(name="N-Gon Count", default=0)
    bpy.types.Scene.fum_isolated_vertex_count = bpy.props.IntProperty(name="Isolated Vertex Count", default=0)
    bpy.types.Scene.fum_preflight_status = bpy.props.StringProperty(name="Preflight Status", default="NONE")
    bpy.types.Scene.fum_preflight_total_issues = bpy.props.IntProperty(name="Preflight Total Issues", default=0)
    bpy.types.Scene.fum_preflight_summary = bpy.props.StringProperty(name="Preflight Summary", default="Run Export Check to validate the active mesh.")


def unregister():
    for property_name in reversed(_SCENE_PROPERTIES):
        if hasattr(bpy.types.Scene, property_name):
            delattr(bpy.types.Scene, property_name)

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
