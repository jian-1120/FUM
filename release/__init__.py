import bpy

from .operators.non_manifold_edges import FUM_OT_DetectNonManifoldEdges
from .operators.duplicate_vertices import FUM_OT_DetectDuplicateVertices
from .ui.panel import VIEW3D_PT_FUMPanel

bl_info = {
    "name": "FUM",
    "author": "Jian",
    "version": (1, 1),
    "blender": (3, 0, 0),
    "location": "3D Viewport > Sidebar > FUM",
    "description": "A collection of mesh analysis tools for Blender.",
    "warning": "",
    "doc_url": "",
    "category": "Mesh",
}

# 注册和注销函数
classes = (
    FUM_OT_DetectNonManifoldEdges,
    FUM_OT_DetectDuplicateVertices,
    VIEW3D_PT_FUMPanel,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
