# FUM v2.0 — Professionalization Update

FUM v2.0 transforms the addon presentation into a more professional, English-first, Blender Market-ready experience. This is not a feature-heavy expansion. The update focuses on polish, consistency, metadata completeness, installation clarity, and repository presentation while preserving the stable v1.6 Export Preflight workflow.

## Release Summary

| Item | Details |
|---|---|
| Version | v2.0 |
| Theme | Professionalization Update |
| Blender Target | Blender 4.x |
| Primary Workflow | Export Preflight |
| Interface Language | English-first |
| License | MIT |

## What Changed

The visible addon interface has been converted to professional English. This includes panel sections, buttons, operator labels, operator descriptions, property labels, reports, warnings, status summaries, and inspection result messages.

| Area | Update |
|---|---|
| UI | Clear English-first panel labels and inspection messages. |
| UX | Export Preflight appears first, followed by summary counters and individual tools. |
| Manifest | Added a completed `blender_manifest.toml` for Blender 4.x metadata. |
| Documentation | Rebuilt README with installation, workflow, feature, and presentation sections. |
| Visual Structure | Prepared `images/banners/`, `images/screenshots/`, and `images/gifs/` for polished future assets. |
| Release Clarity | Added dedicated v2.0 release notes and updated changelog entries. |

## Export Preflight Workflow

The Export Preflight workflow remains intentionally focused. Users select a mesh, click **Run Export Preflight**, and receive a PASS, WARNING, or FAIL result based on the current mesh inspection counters.

| Status | Meaning |
|---|---|
| PASS | The mesh is ready for export. |
| WARNING | Non-blocking issues should be reviewed before export. |
| FAIL | Blocking export issues should be fixed before export. |

## Blender Market Readiness

This update improves the public-facing quality of the repository and addon by aligning the UI with international Blender user expectations, completing modern addon metadata, clarifying installation, and preparing a clean visual asset structure. Future marketplace work can now focus on final screenshots, GIF demonstrations, banner assets, and packaging automation.

## Stability Notes

FUM v2.0 does not add large new systems or expand the feature scope. The existing modular architecture is preserved. Known future engineering opportunities, such as reducing operator coupling and consolidating analysis passes, remain documented in `docs/ENGINEERING_NOTES.md`.
