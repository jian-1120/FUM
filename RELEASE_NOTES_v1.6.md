# FUM v1.6 — Export Preflight Workflow Update

FUM v1.6 stabilizes the addon as an **Export Preflight Workflow** assistant for Blender. This release focuses on validating mesh quality before export to game engines, rendering workflows, and downstream asset pipelines.

## Release Summary

| Item | Details |
|---|---|
| Version | v1.6 |
| Release Theme | Export Preflight Workflow Update |
| Primary Operator | `fum.export_preflight_check` |
| Blender Target | Blender 4.x |
| Export Status Results | PASS, WARNING, FAIL |

## What Changed

The new Export Preflight workflow runs all existing FUM mesh checks from one action. It aggregates non-manifold edge detection, duplicate vertex detection, flipped normal detection, N-Gon detection, and isolated vertex detection into a single export-readiness pass. The result is stored in Scene properties and displayed directly in the FUM panel.

| Check | Severity in Preflight | Reason |
|---|---|---|
| Non-manifold Edges | FAIL | Can break export, collision, shading, or downstream topology processing. |
| Flipped Normals | FAIL | Can cause visible rendering and game-engine shading errors. |
| Duplicate Vertices | WARNING | Often fixable but should be reviewed before export. |
| N-Gons | WARNING | May be acceptable in some workflows but risky for triangulation-dependent pipelines. |
| Isolated Vertices | WARNING | Usually unintended cleanup artifacts that should be reviewed. |

## User Interface

The FUM panel now includes a dedicated **Export Preflight** section. It provides a one-click **Run Export Check** action, a professional PASS/WARNING/FAIL result, total issue count, and per-check counters for quick inspection.

## Engineering Notes

This release keeps the modular addon architecture intact. Operators continue to use `poll()` checks for context safety, inspection state is stored on `bpy.types.Scene`, and individual mesh checks retain safe mode restoration patterns. The legacy full inspection command remains available and now reuses the export preflight workflow for consistent results.

## Repository Hygiene

Internal workflow state files are intentionally excluded from version control and release contents. No binary release assets are attached to this release; GitHub source downloads are generated from the tagged repository state.
