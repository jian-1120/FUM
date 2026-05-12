# Changelog

## FUM v1.6 — Export Preflight Workflow Update

FUM v1.6 introduces a professional **Export Preflight Workflow** for validating meshes before export to game engines, rendering workflows, or downstream production pipelines. The release adds the `fum.export_preflight_check` operator, which runs the full inspection stack and stores a persistent Scene-level result summary for the UI.

| Area | Change |
|---|---|
| Export workflow | Added one-click export readiness validation with PASS, WARNING, and FAIL outcomes. |
| Inspection aggregation | Combined non-manifold edge, duplicate vertex, flipped normal, N-Gon, and isolated vertex checks into a single preflight workflow. |
| UI | Added a dedicated Export Preflight section with total issue count, status messaging, and per-check inspection counters. |
| State management | Added Scene properties for preflight status, total issue count, and human-readable summary text. |
| Compatibility | Prepared the addon metadata for Blender 4.x workflows. |
| Repository hygiene | Ensured internal workflow files are ignored and excluded from version-controlled release contents. |

## FUM v1.5 — Engineering Update

FUM v1.5 improved the technical foundation of the addon by introducing the one-click full inspection system, Scene-based state management, safer mode restoration using `try/finally`, operator `poll()` methods for context safety, and optimized BMesh usage in duplicate vertex detection.

## FUM v1.4

FUM v1.4 added isolated vertices detection, problem vertex highlighting, and expanded mesh inspection coverage.

## FUM v1.3

FUM v1.3 added N-Gon detection, problem face highlighting, and improved the topology inspection workflow.

## FUM v1.2

FUM v1.2 added flipped normals detection, problem face highlighting, and improved the mesh inspection workflow.
