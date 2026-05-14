# FUM Engineering Notes

This document records engineering boundaries for FUM's export preflight architecture and professionalization work. It is intentionally focused on stability, compliance, workflow consistency, and repository hygiene.

## Current Release Focus

| Version | Theme | Engineering Boundary |
|---|---|---|
| v2.0 | Professionalization Update | English-first UI, complete manifest metadata, professional repository presentation, release clarity, and visual asset structure. |
| v1.6 | Export Preflight Workflow Update | Unified inspection workflow with PASS/WARNING/FAIL export readiness status. |

## v2.0 Stabilization Summary

| Area | Status | Notes |
|---|---|---|
| UI language | Complete | Visible UI labels, buttons, operator labels, reports, warnings, and summaries are English-first. |
| Manifest metadata | Complete | `blender_manifest.toml` defines version, author, compatibility, tags, license, and repository link. |
| License compliance | Complete | A repository-level MIT `LICENSE` file is present and matches README license wording. |
| Visual structure | Complete | `images/banners/`, `images/screenshots/`, and `images/gifs/` are prepared for future polished assets. |
| Release scope | Preserved | v2.0 intentionally avoids large feature expansion and keeps the existing inspection architecture stable. |

## Export Preflight Architecture Review

The current preflight workflow reuses existing FUM operators instead of duplicating mesh-analysis logic. This preserves behavior consistency between individual tools, full inspection, and export preflight. The approach is stable for v2.0 but has known future refactor opportunities.

| Risk | Current Impact | Current Mitigation | Future Option |
|---|---|---|---|
| Mode switching overhead | Each inspection operator may enter Edit Mode and restore state, which can add overhead on dense meshes. | The current design prioritizes correctness, highlighting, and predictable user workflow. | Introduce pure analysis helpers that operate on one BMesh pass, then let operators call those helpers. |
| Operator coupling | `fum.export_preflight_check` depends on existing operator IDs and their Scene counters. | This avoids duplicated logic and keeps v2.0 stable. | Move shared detection logic into internal service functions while keeping operators as UI wrappers. |
| UI context dependence | Blender operators require a valid active mesh context and can be sensitive to mode and selection state. | Operators use `poll()` checks and `try/finally` restoration patterns. | Add lower-level context-free analysis functions for automated tests and batch workflows. |
| Selection visibility | Each inspection highlights its own result, and later checks may overwrite earlier selection visibility. | Counts remain preserved in `bpy.types.Scene`, and the UI summary provides the authoritative preflight result. | Add a dedicated issue overlay or grouped issue visualization mode in a future version. |

## Recommended Future Engineering Step

The next meaningful engineering improvement is to separate detection logic from Blender operator execution. A future refactor should introduce reusable analysis functions that return structured issue data, while UI operators remain responsible for selection highlighting, reporting, and user interaction.
