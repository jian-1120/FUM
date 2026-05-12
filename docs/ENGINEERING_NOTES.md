# FUM v1.6 Engineering Notes

This document records stabilization notes for the FUM v1.6 **Export Preflight Workflow Update**. It is intentionally limited to compliance, stability, workflow consistency, and repository hygiene. It does not expand the addon scope beyond the current v1.6 feature set.

## Stabilization Summary

| Area | Status | Notes |
|---|---|---|
| License compliance | Complete | A repository-level MIT `LICENSE` file is present and matches the README license statement. |
| Mesh select mode preservation | Complete | Non-manifold edge and duplicate vertex operators preserve and restore the user's original mesh select mode. |
| Internal workflow files | Complete | Internal workflow state files are ignored and excluded from repository and release downloads. |
| Image structure | Complete | The `images/` folder is retained with a placeholder for future screenshots and GIFs, while broken local demo references were removed. |
| Export preflight stability | Documented | Current architecture is stable for v1.6 but has known future refactor opportunities. |

## Export Preflight Architecture Review

The v1.6 preflight workflow intentionally reuses existing FUM operators instead of duplicating mesh-analysis logic. This keeps behavior consistent across individual tools, full inspection, and export preflight, while preserving the modular addon structure.

| Risk | Current Impact | Current Mitigation | Future Option |
|---|---|---|---|
| Mode switching overhead | Each inspection operator may enter Edit Mode and restore state, which can add overhead on dense meshes. | The current design prioritizes correctness and user-visible highlighting over speed. | Introduce pure analysis helpers that operate on one BMesh pass, then let operators call those helpers. |
| Operator coupling | `fum.export_preflight_check` depends on existing operator IDs and their Scene counters. | This avoids duplicated logic and keeps v1.6 stable. | Move shared detection logic into internal service functions while keeping operators as UI wrappers. |
| UI context dependence | Blender operators require a valid active mesh context and can be sensitive to mode and selection state. | Operators use `poll()` checks and `try/finally` restoration patterns. | Add lower-level context-free analysis functions for automated tests and batch workflows. |
| Selection visibility | Each inspection highlights its own result, and later checks may overwrite earlier selection visibility. | Counts remain preserved in `bpy.types.Scene`, and the UI summary provides the authoritative preflight result. | Add a dedicated issue overlay or grouped issue visualization mode in a future version. |

## Stability Boundary

The current stabilization pass does not introduce a new version number and does not redesign the detection architecture. The recommended next engineering step is to split detection into reusable pure functions and keep Blender operators focused on user interaction, selection highlighting, and reporting.
