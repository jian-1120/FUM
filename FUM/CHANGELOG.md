# Changelog

## FUM v2.0 — Professionalization Update

FUM v2.0 professionalizes the addon for an English-first Blender user experience and a cleaner Blender Market-ready repository presentation. This update intentionally avoids feature bloat and focuses on polish, metadata completeness, UI clarity, and release quality.

| Area | Change |
|---|---|
| UI | Converted visible operator labels, reports, warnings, and panel text to professional English. |
| Manifest | Added a completed Blender 4.x `blender_manifest.toml`. |
| Addon Metadata | Updated `bl_info` to v2.0 with professional description and repository links. |
| Workflow | Preserved the existing Export Preflight workflow while improving naming consistency and summary wording. |
| Repository | Updated documentation, release notes, and visual asset structure for marketplace readiness. |

## FUM v1.6 — Export Preflight Workflow Update

FUM v1.6 added the **Export Preflight Workflow**, a production-oriented mesh validation assistant for checking export readiness before assets move into game engines or other downstream pipelines. The `fum.export_preflight_check` operator runs every existing inspection system, aggregates the results, and stores a clear PASS, WARNING, or FAIL status in Scene properties for persistent UI feedback.

| Area | Change |
|---|---|
| Export workflow | Added one-click export readiness validation. |
| Inspection aggregation | Runs non-manifold edge, duplicate vertex, flipped normal, N-Gon, and isolated vertex checks together. |
| UI | Adds status, total issue count, and per-check counters in the FUM panel. |
| Safety | Keeps context checks through `poll()` methods and uses safe mode restoration across inspection operators. |
| State | Uses `bpy.types.Scene` properties for inspection counters and preflight summary state. |

### v1.6 Stabilization Pass

This stabilization pass added the repository-level MIT `LICENSE` file, restored mesh select mode for non-manifold edge and duplicate vertex detection, removed broken local image references, and documented remaining Export Preflight architecture risks without expanding the v1.6 feature scope.

## FUM v1.5 — Engineering Update

FUM v1.5 introduced the one-click full inspection system, Scene-based state management, safer mode restoration using `try/finally`, `poll()` methods for context safety, and optimized BMesh usage in duplicate vertex detection.

## FUM v1.4

FUM v1.4 added isolated vertices detection, problem vertex highlighting, and enhanced mesh inspection capabilities.

## FUM v1.3

FUM v1.3 added N-Gon detection, problem face highlighting, and improved mesh inspection workflow.

## FUM v1.2

FUM v1.2 added flipped normals detection, problem face highlighting, and improved mesh inspection workflow.
