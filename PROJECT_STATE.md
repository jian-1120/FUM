# FUM Project State

## Current Version
v1.4

## Implemented Systems (v1.4)
- **Non-manifold Edge Detection**: Detects and highlights edges shared by more than two faces or open edges.
- **Duplicate Vertices Detection**: Identifies and highlights vertices that are too close to each other (with adjustable threshold).
- **Flipped Normals Detection**: Detects and highlights faces with normals pointing inwards.
- **N-Gon Detection**: Identifies and highlights faces with more than four edges.
- **Isolated Vertices Detection**: Detects and highlights vertices that are not connected to any edges or faces.

## Planned Systems (Roadmap)
- **Model Quality Scoring System**: A system to evaluate and score the overall quality of a mesh.
- **AI-assisted Optimization Suggestions**: AI-driven recommendations for mesh optimization and repair.

## Repository Status
- **Architecture**: Modular and extensible, with operators and UI panels separated.
- **Installation**: Currently requires manual copying of the inner `FUM` folder due to GitHub's default ZIP packaging behavior. Future plans include automated ZIP packaging for direct Blender installation.
- **Compatibility**: Fully compatible with Blender 4.x.
- **Documentation**: `README.md` and `CHANGELOG.md` are synchronized and provide comprehensive information.

## Development Roadmap
- [x] Non-manifold edge detection
- [x] Duplicate vertices detection
- [x] Flipped normals detection
- [x] N-Gon detection
- [x] Isolated vertices detection
- [ ] Model quality scoring system
- [ ] AI-assisted optimization suggestions
