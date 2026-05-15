# CHANGELOG

## FUM v2.1 — UX Cleanup Update

This update focuses on refining the user experience, simplifying workflows, and strengthening FUM's brand positioning as a professional Blender Market-ready addon.

### UX Improvements

*   **Unified Workflow:** The redundant "Full Inspection" button has been removed from the UI. The "Export Preflight" operator is now the sole entry point for comprehensive mesh validation, streamlining the user experience.
*   **Targeted Inspection Tools:** The individual inspection tools section is now clearly labeled as "Targeted Inspection Tools" to emphasize their role in focused issue review.
*   **Lightweight Repair Suggestions:** Added concise repair suggestions to the detection reports for Non-Manifold Edges, Duplicate Vertices, Flipped Normals, N-Gons, and Isolated Vertices, improving beginner usability without adding complex repair systems.

### Documentation & Branding

*   **Roadmap Integration:** A new "Roadmap" section has been added to `README.md`, outlining FUM's long-term vision as a cross-platform mesh diagnostic standard.
*   **Version Update:** Plugin version updated to `v2.1` across `__init__.py` and `blender_manifest.toml`.
*   **Documentation Cleanup:** `PROJECT_STATE.md` has been removed from the public repository to maintain a professional and minimal codebase.

## FUM v2.0 — Professionalization Update

This major update transforms FUM into a professional, Blender Market-ready addon with an English-first interface and robust metadata.

### UI & UX

*   **English-first UI:** All visible UI text, including panel labels, buttons, operator descriptions, reports, warnings, and summaries, has been converted to professional English, ensuring naming consistency and readability for international users.
*   **Consistent Wording:** Standardized terminology across all UI elements and operator messages.
*   **Predictable Layout:** Panel layout prioritizes export preflight, followed by summary counters, and then individual tools.

### Compliance & Metadata

*   **Complete `blender_manifest.toml`:** The manifest now includes comprehensive metadata such as addon description, version, author, Blender compatibility (4.x), category, license, and website/repository links.
*   **MIT License:** A proper `LICENSE` file has been added to the repository, ensuring legal compliance and consistency with `README.md`.

### Repository & Release Hygiene

*   **Professional `README.md`:** The main `README.md` has been restructured for a professional presentation, including installation guides, feature showcases, workflow explanations, and export preflight details.
*   **Visual Assets Structure:** A clean `images/` directory structure (`banners/`, `screenshots/`, `gifs/`) has been prepared for future marketing materials, with `images/README.md` providing clear guidance.
*   **Internal File Cleanup:** Ensured `PROJECT_STATE.md` is excluded from the repository and releases.
*   **Release Notes Quality:** `RELEASE_NOTES_v2.0.md` provides a clear summary of the update.

## FUM v1.6 — Export Preflight Workflow Update

FUM v1.6 added the **Export Preflight Workflow**, a production-oriented mesh validation assistant for checking export readiness before assets move into game engines or other downstream pipelines. The `fum.export_preflight_check` operator runs every existing inspection system, aggregates the results, and stores a clear PASS, WARNING, or FAIL status in Scene properties for persistent UI feedback.

### Engineering & Stability

*   **Export Preflight Operator:** Implemented `fum.export_preflight_check` for a unified full inspection workflow.
*   **Integrated Inspection:** All individual inspection operators are now integrated into the preflight check.
*   **Clean Summary:** Provides a clear, aggregated inspection summary in the UI.
*   **Operator Safety:** Ensured all operators include `poll()` methods and `try/finally` blocks for robust error handling and state restoration.
*   **Selection Mode Restoration:** Fixed `non_manifold_edges.py` and `duplicate_vertices.py` to correctly restore the user's original mesh select mode after execution.

### Documentation & Repository

*   **`README.md` Update:** Updated `README.md` with v1.6 feature descriptions, usage examples, and version information.
*   **`CHANGELOG.md` Update:** Documented v1.6 changes in `CHANGELOG.md`.
*   **`RELEASE_NOTES_v1.6.md`:** Created formal release notes for v1.6.
*   **`.gitignore` Enhancement:** Expanded `.gitignore` to exclude internal workflow files, caches, build artifacts, and local environment files.
*   **`PROJECT_STATE.md` Removal:** Ensured `PROJECT_STATE.md` is not present in the repository, releases, or downloadable packages.
*   **Repository Structure:** Verified a clean and professional repository structure.

## FUM v1.5 — Initial Release

Initial release of FUM with core mesh inspection functionalities.

### Features

*   Non-manifold edge detection
*   Duplicate vertex detection
*   Flipped normal detection
*   N-Gon detection
*   Isolated vertex detection
*   Basic UI panel for running inspections
