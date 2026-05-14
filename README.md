# FUM — Fix Your Mesh

**FUM** is a professional Blender addon for mesh inspection and export preflight validation. It helps artists, environment designers, technical artists, and asset pipeline teams identify common geometry issues before models are exported to game engines, rendering workflows, or downstream production tools.

## Version

| Field | Value |
|---|---|
| Current Version | v2.0 |
| Release Theme | Professionalization Update |
| Blender Target | Blender 4.x |
| License | MIT License |
| Repository | <https://github.com/jian-1120/FUM> |

## What FUM Does

FUM focuses on practical mesh quality checks that are commonly reviewed before export. The addon provides individual inspection tools as well as a unified **Export Preflight** workflow that summarizes the active mesh as **PASS**, **WARNING**, or **FAIL**.

| Inspection | Purpose | Preflight Severity |
|---|---|---|
| Non-Manifold Edges | Finds edges that can break topology, collision, shading, or export workflows. | FAIL |
| Duplicate Vertices | Finds vertices closer than a configurable threshold. | WARNING |
| Flipped Normals | Finds faces whose normals appear inverted compared with recalculated normals. | FAIL |
| N-Gons | Finds faces with more than four vertices. | WARNING |
| Isolated Vertices | Finds loose vertices with no connected edges. | WARNING |

## Export Preflight Workflow

The **Export Preflight** workflow is designed as a final check before asset handoff. Click **Run Export Preflight** in the FUM panel to run all inspections, update issue counters, and display a clear export-readiness summary.

| Status | Meaning | Recommended Action |
|---|---|---|
| PASS | No known mesh issues were found. | The mesh is ready for export. |
| WARNING | Non-blocking issues were found. | Review the highlighted geometry before export. |
| FAIL | Blocking export issues were found. | Fix the reported issues before export. |

> FUM does not automatically modify your mesh. It detects, highlights, and summarizes potential problems so artists remain in control of the final cleanup process.

## Installation

Download the latest release from the [GitHub Releases page](https://github.com/jian-1120/FUM/releases/latest). If you download the source ZIP from GitHub, install the inner `FUM` folder that contains `__init__.py`, `operators/`, `ui/`, and `blender_manifest.toml`.

| Step | Action |
|---|---|
| 1 | Download or clone the repository. |
| 2 | Locate the inner `FUM` addon folder. |
| 3 | Copy the `FUM` folder into Blender's addons directory, or install it through Blender's Add-ons preferences. |
| 4 | Enable **FUM - Fix Your Mesh** in `Edit > Preferences > Add-ons`. |
| 5 | Open the 3D Viewport sidebar with `N`, then select the **FUM** tab. |

Typical Blender addon directories are shown below.

| Platform | Addon Directory |
|---|---|
| Windows | `C:\Users\<username>\AppData\Roaming\Blender Foundation\Blender\<version>\scripts\addons\` |
| macOS | `/Users/<username>/Library/Application Support/Blender/<version>/scripts/addons/` |
| Linux | `~/.config/blender/<version>/scripts/addons/` |

## User Workflow

FUM is built around a simple inspection loop. Select a mesh object, open the **FUM** sidebar panel, run **Export Preflight**, and review the status summary. If the result is **WARNING** or **FAIL**, use the individual inspection tools to focus on a specific issue category and review the highlighted geometry in Edit Mode.

## UI and UX Principles

Version 2.0 introduces an English-first interface for international Blender users. Panel labels, buttons, operator names, reports, warnings, summaries, and property names are written in clear professional English. The UI prioritizes a predictable order: export preflight first, summary counters second, individual tools last.

## Visual Assets

The repository includes an `images/` directory prepared for future Blender Market presentation assets.

| Directory | Intended Content |
|---|---|
| `images/banners/` | Store future marketplace banners and repository headers. |
| `images/screenshots/` | Store UI screenshots and feature previews. |
| `images/gifs/` | Store workflow demonstrations and short animated previews. |

Current preview images are hosted through GitHub attachments to keep the repository lightweight until final marketing assets are prepared.

> <img width="841" height="727" alt="FUM mesh inspection preview" src="https://github.com/user-attachments/assets/35e47d0a-22c7-4797-b23a-11cbe4743970" /><img width="621" height="749" alt="FUM interface preview" src="https://github.com/user-attachments/assets/c433c826-61c4-4891-a5dc-32acee7e1a27" />

## Repository Structure

```text
FUM/
├── FUM/
│   ├── __init__.py
│   ├── blender_manifest.toml
│   ├── operators/
│   │   ├── duplicate_vertices.py
│   │   ├── export_preflight.py
│   │   ├── flipped_normals.py
│   │   ├── full_inspection.py
│   │   ├── isolated_vertices.py
│   │   ├── ngons.py
│   │   └── non_manifold_edges.py
│   └── ui/
│       └── panel.py
├── docs/
│   └── ENGINEERING_NOTES.md
├── images/
│   ├── banners/
│   ├── gifs/
│   └── screenshots/
├── CHANGELOG.md
├── LICENSE
├── README.md
└── RELEASE_NOTES_v2.0.md
```

## Release Packaging Notes

For manual installation, the inner `FUM` folder is the Blender addon folder. For future marketplace packaging, the package should preserve `__init__.py`, `blender_manifest.toml`, `operators/`, `ui/`, and the MIT `LICENSE` file. Internal workflow files and generated build artifacts are excluded through `.gitignore`.

## Roadmap

| Status | Item |
|---|---|
| Complete | Non-manifold edge detection |
| Complete | Duplicate vertex detection |
| Complete | Flipped normals detection |
| Complete | N-Gon detection |
| Complete | Isolated vertex detection |
| Complete | Export Preflight workflow |
| Complete | English-first professional UI pass |
| Planned | Mesh quality scoring system |
| Planned | Guided cleanup suggestions |

## License

FUM is released under the MIT License. See [`LICENSE`](LICENSE) for the full license text.

## Author

FUM is developed by **Jian**, an environment design student exploring AI-assisted modeling workflows and practical 3D production tools.
