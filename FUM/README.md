# FUM Addon Folder

This is the installable **FUM - Fix Your Mesh** Blender addon folder. It contains the addon entry point, Blender 4.x manifest, operators, and UI code.

## Version

| Field | Value |
|---|---|
| Addon | FUM - Fix Your Mesh |
| Version | v2.0 |
| Release Theme | Professionalization Update |
| Blender Target | Blender 4.x |
| Interface Language | English-first |

## Installation

Install this inner `FUM` folder in Blender. The correct folder is the one that contains `__init__.py`, `blender_manifest.toml`, `operators/`, and `ui/`.

| Step | Action |
|---|---|
| 1 | Copy the entire `FUM` folder into Blender's addons directory, or install it through Blender preferences. |
| 2 | Open `Edit > Preferences > Add-ons`. |
| 3 | Search for `FUM` and enable **FUM - Fix Your Mesh**. |
| 4 | Open the 3D Viewport sidebar with `N` and use the **FUM** tab. |

## v2.0 Professionalization Update

FUM v2.0 focuses on professional presentation and international usability. The visible UI, buttons, operator labels, reports, warnings, and summaries are now written in clear English. The addon also includes a completed Blender 4.x `blender_manifest.toml` for modern addon metadata.

The main workflow remains intentionally focused: select a mesh, run **Export Preflight**, review the PASS/WARNING/FAIL result, and use individual inspection tools when targeted review is needed.
