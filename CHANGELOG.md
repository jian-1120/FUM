# Changelog

## FUM v2.0 — Professionalization Update

FUM v2.0 prepares the addon for a more professional Blender Marketplace-style presentation without expanding the feature scope. The release focuses on international usability, metadata completeness, repository presentation, and workflow consistency.

| Area | Change |
|---|---|
| UI Internationalization | Converted visible panel labels, buttons, operator labels, reports, warnings, and summaries to professional English. |
| Addon Metadata | Updated addon metadata to v2.0 and added a completed Blender 4.x `blender_manifest.toml`. |
| UX Consistency | Improved panel ordering, Export Preflight wording, status presentation, and individual tool labeling. |
| Repository Presentation | Rebuilt README with professional installation, workflow, feature, visual asset, and release packaging sections. |
| Visual Structure | Prepared `images/banners/`, `images/screenshots/`, and `images/gifs/` for future marketplace presentation assets. |
| Release Quality | Added v2.0 release notes and preserved clean release packaging expectations. |

## FUM v1.6 — Export Preflight Workflow Update

FUM v1.6 introduced a professional **Export Preflight Workflow** for validating meshes before export to game engines, rendering workflows, or downstream production pipelines. The release added the `fum.export_preflight_check` operator, which runs the full inspection stack and stores a persistent Scene-level result summary for the UI.

| Area | Change |
|---|---|
| Export workflow | Added one-click export readiness validation with PASS, WARNING, and FAIL outcomes. |
| Inspection aggregation | Combined non-manifold edge, duplicate vertex, flipped normal, N-Gon, and isolated vertex checks into a single preflight workflow. |
| UI | Added a dedicated Export Preflight section with total issue count, status messaging, and per-check inspection counters. |
| State management | Added Scene properties for preflight status, total issue count, and human-readable summary text. |
| Compatibility | Prepared the addon metadata for Blender 4.x workflows. |
| Repository hygiene | Ensured internal workflow files are ignored and excluded from version-controlled release contents. |

### v1.6 Stabilization Pass

This stabilization pass added the missing MIT `LICENSE` file, restored mesh select mode in the non-manifold edge and duplicate vertex operators, cleaned broken local image references, prepared a minimal `images/` directory for future media, and documented current Export Preflight architecture risks in `docs/ENGINEERING_NOTES.md`.

## FUM v1.5 — Engineering Update

FUM v1.5 improved the technical foundation of the addon by introducing the one-click full inspection system, Scene-based state management, safer mode restoration using `try/finally`, operator `poll()` methods for context safety, and optimized BMesh usage in duplicate vertex detection.

## FUM v1.4

FUM v1.4 added isolated vertices detection, problem vertex highlighting, and expanded mesh inspection coverage.

## FUM v1.3

FUM v1.3 added N-Gon detection, problem face highlighting, and improved the topology inspection workflow.

## FUM v1.2

FUM v1.2 added flipped normals detection, problem face highlighting, and improved the mesh inspection workflow.
