# Contributing to Awesome-AIGC-3D v2

Thank you for contributing! This repository is the companion to our ACM Computing Surveys paper *"From Visual Synthesis to Interactive Worlds: A Survey of Production-Ready 3D Generation"*.

## How to Add a Paper

### 1. Add BibTeX

Create a file `citations/<your-project>.txt` with the BibTeX entry:

```bibtex
@inproceedings{authorYEARkeyword,
  title={Your Paper Title},
  author={Author, First and Author, Second},
  booktitle={Proc. CVPR},
  year={2025}
}
```

### 2. Add to README

Find the appropriate section based on our taxonomy and add your paper in the following format:

```markdown
- **Your Paper Title**, Author et al., Venue Year | [Paper](arxiv-link) | [Code](github-link) | [Project](project-page) | [BibTeX](./citations/your-project.txt)
```

### Taxonomy Guide

Choose the section that best fits your paper:

| Topic | README Section |
|-------|---------------|
| Object geometry generation (SDS, multi-view, diffusion, feed-forward) | General Objects > Geometry Generation |
| Mesh generation, retopology, quad meshing | General Objects > Topology Generation |
| Texture, UV, PBR material generation | General Objects > Appearance Generation |
| Full-body avatar, parametric models, 3DGS avatars | Characters & Avatars > Full-Body / Head & Face |
| Automatic rigging, skinning, animation | Characters & Avatars > Rigging & Skinning |
| Indoor/outdoor layout, scene arrangement | Scenes > Layout Generation |
| Asset placement, scene population | Scenes > Scene Grounding |
| Terrain, skybox, city-scale generation | Scenes > World-Scale |
| Interactive/playable worlds, physics-aware | Scenes > Playable Worlds |
| Datasets, benchmarks, evaluation metrics | Data Foundations / Evaluation |

### 3. Submit a Pull Request

- Target the `v2` branch (not `main`)
- Keep changes focused (one paper per PR is fine)
- Ensure links are working

## Reporting Issues

If you find broken links, misclassified papers, or missing entries, please open an issue.
