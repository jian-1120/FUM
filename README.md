# FUM — Fix Your Mesh

**A Blender mesh validation pipeline tool.**

FUM is designed to empower Technical Artists, 3D Asset Authors, and Pipeline Teams to ensure the integrity and export-readiness of their geometry before models are shipped to game engines, render farms, or any downstream production tools. It transforms the often tedious process of mesh inspection into an efficient, reliable validation step, making it an indispensable part of your 3D production workflow.

## 🎯 Target Users

*   **Technical Artists:** Ensure assets meet technical specifications and reduce rework.
*   **3D Asset Authors:** Validate model quality and elevate delivery standards.
*   **Pipeline Teams:** Standardize mesh quality across teams and optimize production workflows.
*   **Game Asset Creators:** Ensure models perform optimally in game engines and prevent runtime issues.
*   **3D Printing Creators:** Verify models are suitable for 3D printing, avoiding physical defects.

## 🚀 Core Feature: The Export Preflight Workflow

The core strength of FUM lies in its unique **Export Preflight Workflow**. Going beyond simple mesh checking, it provides a unified validation system that rapidly assesses the export-readiness of your active mesh, summarizing its status with clear **PASS**, **WARNING**, or **FAIL** states.

This workflow significantly enhances production reliability by identifying and highlighting potential issues early, thereby preventing costly fixes and project delays further down the pipeline.

| Status | Meaning | Recommended Action |
|---|---|---|
| **PASS** | No known mesh issues were detected. | Your mesh is ready for export. |
| **WARNING** | Non-blocking issues were detected. | Review the highlighted geometry before export. |
| **FAIL** | Blocking export issues were detected. | Fix the reported issues before export. |

> FUM does not automatically modify your mesh. It detects, highlights, and summarizes potential problems, empowering artists to remain in control of the final cleanup process.

## 💡 FUM vs. Blender Native Tools

Blender's native tools offer fundamental mesh selection capabilities, but they are often:

*   **Fragmented:** Requiring navigation between multiple menus and modes.
*   **Manual:** Relying on the user to manually trigger and interpret results.
*   **Not Workflow-Oriented:** Lacking a unified, export-centric validation process.

In contrast, FUM provides:

*   **A Unified Validation Workflow:** Run all critical checks with a single click.
*   **PASS/WARNING/FAIL System:** Clear and intuitive feedback on export readiness.
*   **Export-Oriented Inspection:** Focused on common mesh issues encountered in production environments.

FUM integrates these disparate checks into one efficient pipeline tool, significantly boosting productivity and model quality.

## ⬇️ Installation Guide

1.  Download the latest `FUM_vX.X.zip` file from the [GitHub Releases page](https://github.com/jian-1120/FUM/releases/latest).
2.  In Blender, go to `Edit > Preferences > Add-ons`.
3.  Click the `Install...` button and select the `FUM_vX.X.zip` file you downloaded.
4.  Enable the **FUM - Fix Your Mesh** add-on.
5.  In the 3D Viewport, press `N` to open the sidebar, and you will find the **FUM** panel.

## 🖼️ Visual Assets

### Product Banner

<!-- Placeholder for Product Banner Image -->

### Demo GIF

<!-- Placeholder for Demo GIF -->

### Feature Screenshots

<!-- Placeholder for Feature Screenshot 1 -->

<!-- Placeholder for Feature Screenshot 2 -->

<!-- Placeholder for Feature Screenshot 3 -->

<!-- Placeholder for Feature Screenshot 4 -->

## 🗺️ Future Direction

*   **Future:** FUM Pro for Blender (with advanced repair guidance, batch processing, custom validation profiles, and pipeline integration)

## License

FUM is released under the GNU General Public License v3.0. See [`LICENSE`](LICENSE) for the full license text.

## Author

FUM is developed by **Jian – 3D tools developer**.

## Version Information

| Field | Value |
|---|---|
| Current Version | v2.2 |
| Release Theme | Commercial Packaging Update |
| Blender Target | Blender 4.x |
| License | GPLv3 |
| Repository | <https://github.com/jian-1120/FUM> |
