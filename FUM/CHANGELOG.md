# Changelog

## FUM v1.6 — Export Preflight Workflow Update

FUM v1.6 adds the **Export Preflight Workflow**, a production-oriented mesh validation assistant for checking export readiness before assets move into game engines or other downstream pipelines. The new `fum.export_preflight_check` operator runs every existing inspection system, aggregates the results, and stores a clear PASS, WARNING, or FAIL status in Scene properties for persistent UI feedback.

| Area | Change |
|---|---|
| Export workflow | Added one-click export readiness validation. |
| Inspection aggregation | Runs non-manifold edge, duplicate vertex, flipped normal, N-Gon, and isolated vertex checks together. |
| UI | Adds status, total issue count, and per-check counters in the FUM panel. |
| Safety | Keeps context checks through `poll()` methods and uses safe mode restoration across inspection operators. |
| State | Uses `bpy.types.Scene` properties for inspection counters and preflight summary state. |

### v1.6 Stabilization Pass

This stabilization pass adds the repository-level MIT `LICENSE` file, restores mesh select mode for non-manifold edge and duplicate vertex detection, removes broken local image references, and documents remaining Export Preflight architecture risks without expanding the v1.6 feature scope.

## FUM v1.5 — Engineering Update

FUM v1.5 introduced the one-click full inspection system, Scene-based state management, safer mode restoration using `try/finally`, `poll()` methods for context safety, and optimized BMesh usage in duplicate vertex detection.

## FUM v1.4

FUM v1.4 added isolated vertices detection, problem vertex highlighting, and enhanced mesh inspection capabilities.

## FUM v1.3

FUM v1.3 added N-Gon detection, problem face highlighting, and improved mesh inspection workflow.

## FUM v1.2

FUM v1.2 added flipped normals detection, problem face highlighting, and improved mesh inspection workflow.
