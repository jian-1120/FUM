# FUM — Fix Your Mesh

**A Blender mesh validation pipeline tool.**

FUM helps artists and production teams validate mesh quality before export. It is designed around a clear **Export Preflight Workflow** that checks common geometry issues, summarizes the active mesh with **PASS**, **WARNING**, or **FAIL** states, and gives users a focused review step before assets move into game engines, rendering workflows, 3D printing preparation, or downstream production pipelines.

The goal of FUM is not to replace artistic judgment or automatically alter geometry. Instead, it provides a consistent validation layer that makes mesh review easier to repeat, easier to understand, and easier to integrate into a professional Blender workflow.

## Product Focus

FUM is built for export reliability. Rather than presenting mesh checks as scattered tools, it organizes validation around a single preflight process that helps users understand whether an asset is ready to move forward.

| Area | FUM Approach |
|---|---|
| Workflow | A unified export preflight process for validating the active mesh. |
| Feedback | Clear PASS, WARNING, and FAIL states for export-readiness review. |
| Inspection | Focused checks for common geometry issues that can affect production handoff. |
| Control | Detection and highlighting without automatically modifying user geometry. |

## Target Users

FUM is intended for Blender users who need predictable mesh validation before export. Technical artists can use it to check assets against production expectations, 3D asset authors can use it to improve delivery quality, and pipeline teams can use it as a lightweight quality-control step in a broader asset workflow.

| User Group | Typical Value |
|---|---|
| Technical Artists | Quickly review geometry problems before handoff or integration. |
| 3D Asset Authors | Validate model quality before delivery. |
| Pipeline Teams | Standardize a repeatable mesh validation step. |
| Game Asset Creators | Identify geometry issues before engine import. |
| 3D Printing Creators | Review common mesh problems before print preparation. |

## Export Preflight Workflow

The **Export Preflight Workflow** is the primary FUM experience. It runs the supported inspection checks, updates issue counters, and reports the overall export-readiness state of the active mesh.

| Status | Meaning | Recommended Action |
|---|---|---|
| **PASS** | No known mesh issues were detected. | The mesh is ready for export review. |
| **WARNING** | Non-blocking issues were detected. | Review the highlighted geometry before export. |
| **FAIL** | Blocking export issues were detected. | Fix the reported issues before export. |

FUM currently checks for non-manifold edges, duplicate vertices, flipped normals, N-gons, and isolated vertices. These checks are presented as part of the preflight workflow and are also available as targeted inspection tools for focused review.

## FUM Compared with Blender Native Tools

Blender includes powerful native mesh selection and cleanup capabilities, but many checks are spread across different menus, modes, and manual operations. FUM is designed to make validation more workflow-oriented by grouping common checks into a single export-focused process.

| Blender Native Tools | FUM |
|---|---|
| Often require manual navigation across different tools and modes. | Provides a unified validation workflow. |
| Results may depend on user interpretation and repeated manual steps. | Reports clear PASS, WARNING, and FAIL states. |
| General-purpose modeling tools. | Export-oriented mesh validation for production review. |

FUM complements Blender’s existing toolset by making common validation steps easier to run consistently before export.

## Installation

Download the latest `FUM_vX.X.zip` file from the [GitHub Releases page](https://github.com/jian-1120/FUM/releases/latest). In Blender, open `Edit > Preferences > Add-ons`, click `Install...`, select the downloaded ZIP file, and enable **FUM - Fix Your Mesh**. Once enabled, open the 3D Viewport sidebar with `N` and select the **FUM** tab.

The release ZIP is packaged with the Blender add-on folder at the top level, so it can be installed directly through Blender without extracting repository files manually.

## Visual Assets

The repository includes an `images/` directory for product screenshots, workflow GIFs, and banner artwork. Visual assets can be added as they become available without changing the add-on package structure.

## Future Direction

Future development is focused on **FUM Pro for Blender**, with advanced repair guidance as the primary direction. Additional capabilities will be considered only when they support the core validation workflow and preserve add-on stability.

## License

FUM is released under the GNU General Public License v3.0. See [`LICENSE`](LICENSE) for the full license text.

## Author

FUM is developed by **Jian – 3D tools developer**.

## Repository

Project repository: <https://github.com/jian-1120/FUM>
