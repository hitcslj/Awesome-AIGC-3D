# From Visual Synthesis to Interactive Worlds <br> A Survey of Production-Ready 3D Generation

[![arXiv](https://img.shields.io/badge/arXiv-2026.xxxxx-b31b1b.svg)](https://arxiv.org/abs/2026.xxxxx)
[![ACM CSUR](https://img.shields.io/badge/ACM-Computing%20Surveys-blue)](https://dl.acm.org/)
[![Project Page](https://img.shields.io/badge/Project-Page-green)](https://christinebobby.github.io/production-ready-3d-survey/)
[![GitHub stars](https://img.shields.io/github/stars/hitcslj/Awesome-AIGC-3D?style=social)](https://github.com/hitcslj/Awesome-AIGC-3D)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

<p align="center">
  <img src="asset/fig1_pipeline.jpg" width="100%">
</p>

## News

- **[2026-04]** v2.0: ACM Computing Surveys companion release with production-pipeline taxonomy
- **[2025-08]** v1.0: Original awesome list by Jian Liu (available on [main branch](https://github.com/hitcslj/Awesome-AIGC-3D/tree/main))

## Abstract

Three-dimensional content generation has progressed from producing isolated, visually plausible shapes to constructing structured assets that can be deployed in real-time interactive environments. This trajectory is driven by converging demands from game development, embodied AI, world simulation, digital twins, and spatial computing, all of which require 3D content that goes beyond surface appearance to satisfy engine-level constraints on topology, UV parameterization, physically based materials, skeletal rigging, and physics-aware scene layout. Despite rapid advances in generative modeling, a persistent gap separates the outputs of current methods from the production-ready standard expected by interactive applications. This survey addresses that gap by organizing the literature around the asset production pipeline rather than algorithmic families.

---

## Table of Contents

- [Survey Taxonomy](#survey-taxonomy)
- [Data Foundations & Benchmarks](#data-foundations--benchmarks)
  - [Object Datasets](#object-datasets)
  - [Character Datasets](#character-datasets)
  - [Scene Datasets](#scene-datasets)
- [General Objects & Props](#general-objects--props)
  - [Geometry Generation](#geometry-generation)
  - [Topology Generation](#topology-generation)
  - [Appearance Generation](#appearance-generation)
- [Characters & Avatars](#characters--avatars)
  - [Structural Priors](#structural-priors)
  - [Full-Body Synthesis](#full-body-synthesis)
  - [Head & Face Synthesis](#head--face-synthesis)
  - [Rigging & Skinning](#rigging--skinning)
- [Scenes & Environments](#scenes--environments)
  - [Layout Generation](#layout-generation)
  - [Scene Population & Asset Grounding](#scene-population--asset-grounding)
  - [World-Scale Generation](#world-scale-generation)
- [Evaluation & Benchmarks](#evaluation--benchmarks)
- [Industry & Companies](#industry--companies)
- [Citation](#citation)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)
- [v1 Paper Collection](#v1-paper-collection)
- [Star History](#star-history)

---

## Survey Taxonomy

<p align="center">
  <img src="asset/fig2_taxonomy.png" width="100%">
</p>

The survey is organized around a **two-dimensional taxonomy**:

- **Horizontal axis (asset types):** General Objects, Characters & Avatars, Scenes & Environments
- **Vertical axis (pipeline stages):** Data Foundations &rarr; Geometry &rarr; Topology &rarr; UV &rarr; PBR Materials &rarr; Rigging &rarr; Scene Assembly

This structure mirrors the production pipeline used in game engines and interactive applications, enabling direct assessment of where each method fits within a deployment workflow.

---

## Data Foundations & Benchmarks

### Object Datasets

| Dataset | Year | Scale | Description |
|---------|------|-------|-------------|
| [ShapeNet](https://shapenet.org/) | 2015 | 51K models, 55 categories | Large-scale 3D shape repository (Chang et al.) |
| [ModelNet](https://modelnet.cs.princeton.edu/) | 2015 | 12K CAD models, 40 categories | Princeton 3D object benchmark (Wu et al.) |
| [ABC](https://deep-geometry.github.io/abc-dataset/) | 2019 | 1M+ CAD models | Mechanical parts with parametric annotations (Koch et al.) |
| [GSO (Google Scanned Objects)](https://app.gazebosim.org/GoogleResearch/fuel/collections/Scanned%20Objects%20by%20Google%20Research) | 2022 | 1K+ scans | Household objects with PBR materials (Downs et al.) |
| [ABO (Amazon Berkeley Objects)](https://amazon-berkeley-objects.s3.amazonaws.com/index.html) | 2022 | 8K+ models | Product catalog with multi-view images (Collins et al.) |
| [Objaverse](https://objaverse.allenai.org/) | 2023 | 800K+ objects | Internet-scale 3D asset collection (Deitke et al.) |
| [Objaverse-XL](https://objaverse.allenai.org/) | 2024 | 10.2M objects | Extended internet-scale collection (Deitke et al.) |

### Character Datasets

| Dataset | Year | Scale | Description |
|---------|------|-------|-------------|
| [FAUST](http://faust.is.tue.mpg.de/) | 2014 | 300 scans, 10 subjects | Real body scans with ground-truth correspondence (Bogo et al.) |
| [AMASS](https://amass.is.tue.mpg.de/) | 2019 | Large-scale motion capture | Unified motion capture archive (Mahmood et al.) |
| [CAPE](https://cape.is.tue.mpg.de/) | 2020 | 4D clothing | Clothed body scans with pose variation (Ma et al.) |
| [THuman2.0](https://github.com/ytrock/THuman2.0-Dataset) | 2021 | 526 high-res scans | Detailed textured human models (Yu et al.) |
| [HuMMan](https://caizhongang.github.io/projects/HuMMan/) | 2022 | 1K subjects | Multi-modal human dataset (Cai et al.) |
| [Motion-X](https://motion-x-dataset.github.io/) | 2024 | Large-scale motion | Expressive whole-body motion dataset (Lin et al.) |

### Scene Datasets

| Dataset | Year | Scale | Description |
|---------|------|-------|-------------|
| [ScanNet](http://www.scan-net.org/) | 2017 | 1,513 indoor scans | RGB-D reconstructions with annotations (Dai et al.) |
| [Matterport3D](https://niessner.github.io/Matterport/) | 2017 | 90 buildings | Large-scale indoor environments (Chang et al.) |
| [3D-FRONT](https://tianchi.aliyun.com/specials/promotion/alibaba-3d-scene-dataset) | 2021 | 18K rooms | Professionally designed indoor layouts (Fu et al.) |
| [ProcTHOR](https://procthor.allenai.org/) | 2022 | Procedural houses | Infinitely scalable simulated interiors (Deitke et al.) |
| [Infinigen](https://infinigen.org/) | 2023 | Procedural nature | Photorealistic procedural generation of natural worlds (Raistrick et al.) |
| [Infinigen Indoors](https://infinigen.org/) | 2024 | Procedural interiors | Indoor extension of Infinigen (Raistrick et al.) |

---

## General Objects & Props

### Geometry Generation

#### Score Distillation (SDS)

- **DreamFusion**, Poole et al., ICLR 2023 | [Paper](https://arxiv.org/abs/2209.14988) | [Project](https://dreamfusion3d.github.io/) | [BibTeX](./citations/dreamfusion.txt)
- **Magic3D**, Lin et al., CVPR 2023 | [Paper](https://arxiv.org/abs/2211.10440) | [Project](https://research.nvidia.com/labs/dir/magic3d/) | [BibTeX](./citations/magic3d.txt)
- **Fantasia3D**, Chen et al., ICCV 2023 | [Paper](https://arxiv.org/abs/2303.13873) | [Code](https://github.com/Gorilla-Lab-SCUT/Fantasia3D) | [BibTeX](./citations/fantasia3d.txt)
- **ProlificDreamer**, Wang et al., NeurIPS 2023 | [Paper](https://arxiv.org/abs/2305.16213) | [Code](https://github.com/thu-ml/prolificdreamer) | [BibTeX](./citations/prolificdreamer.txt)
- **RichDreamer**, Qiu et al., CVPR 2024 | [Paper](https://arxiv.org/abs/2311.16918) | [Code](https://github.com/modelscope/richdreamer) | [BibTeX](./citations/richdreamer.txt)

#### Multi-View Reconstruction (MV)

- **Zero-1-to-3**, Liu et al., ICCV 2023 | [Paper](https://arxiv.org/abs/2303.11328) | [Code](https://github.com/cvlab-columbia/zero123) | [BibTeX](./citations/zero123.txt)
- **MVDream**, Shi et al., ICML 2024 | [Paper](https://arxiv.org/abs/2308.16512) | [Code](https://github.com/bytedance/MVDream) | [BibTeX](./citations/mvdream.txt)
- **Wonder3D**, Long et al., CVPR 2024 | [Paper](https://arxiv.org/abs/2310.15008) | [Code](https://github.com/xxlong0/Wonder3D) | [BibTeX](./citations/wonder3d.txt)
- **SV3D**, Voleti et al., ECCV 2024 | [Paper](https://arxiv.org/abs/2403.12008) | [Project](https://sv3d.github.io/) | [BibTeX](./citations/sv3d.txt)

#### GAN-based

- **3D-GAN**, Wu et al., NeurIPS 2016 | [Paper](https://arxiv.org/abs/1610.07584) | [BibTeX](./citations/wu2016learning.txt)
- **Tree-GAN**, Shu et al., 2019 | [Paper](https://arxiv.org/abs/1905.06292) | [BibTeX](./citations/shu20193d.txt)
- **SP-GAN**, Li et al., ICCV 2021 | [Paper](https://arxiv.org/abs/2108.04476) | [BibTeX](./citations/li2021sp.txt)
- **SDF-StyleGAN**, Zheng et al., CVPR 2022 | [Paper](https://arxiv.org/abs/2206.12055) | [BibTeX](./citations/zheng2022sdfstylegan.txt)

#### VAE / AE

- **AtlasNet**, Groueix et al., CVPR 2018 | [Paper](https://arxiv.org/abs/1802.05384) | [Code](https://github.com/ThibaultGROUEIX/AtlasNet) | [BibTeX](./citations/groueix2018papier.txt)
- **TM-Net**, Gao et al., 2021 | [Paper](https://arxiv.org/abs/2104.06302) | [BibTeX](./citations/gao2021tm.txt)
- **Michelangelo**, Zhao et al., NeurIPS 2023 | [Paper](https://arxiv.org/abs/2306.17115) | [Code](https://github.com/NeuralCarver/Michelangelo) | [BibTeX](./citations/michelangelo.txt)
- **CLAY**, Zhang et al., 2024 | [Paper](https://arxiv.org/abs/2406.13897) | [BibTeX](./citations/clay.txt)

#### Direct 3D Diffusion

- **PC-DPM**, Luo et al., ICLR 2021 | [Paper](https://arxiv.org/abs/2103.01458) | [BibTeX](./citations/luo2021diffusion.txt)
- **MeshDiffusion**, Liu et al., ICLR 2023 | [Paper](https://arxiv.org/abs/2303.08133) | [Code](https://github.com/lzzcd001/MeshDiffusion) | [BibTeX](./citations/meshdiffusion.txt)
- **TetraDiffusion**, Kalischek et al., 2024 | [Paper](https://arxiv.org/abs/2411.18629) | [BibTeX](./citations/kalischek2024tetradiffusion.txt)

#### Feed-Forward (FF)

- **Pixel2Mesh**, Wang et al., ECCV 2018 | [Paper](https://arxiv.org/abs/1804.01654) | [Code](https://github.com/nywang16/Pixel2Mesh) | [BibTeX](./citations/wang2018pixel2mesh.txt)
- **LRM**, Hong et al., ICLR 2024 | [Paper](https://arxiv.org/abs/2311.04400) | [Project](https://yiconghong.me/LRM/) | [BibTeX](./citations/lrm.txt)
- **TripoSR**, Tochilkin et al., 2024 | [Paper](https://arxiv.org/abs/2403.02151) | [Code](https://github.com/VAST-AI-Research/TripoSR) | [BibTeX](./citations/TripoSR2024.txt)
- **InstantMesh**, Xu et al., 2024 | [Paper](https://arxiv.org/abs/2404.07191) | [Code](https://github.com/TencentARC/InstantMesh) | [BibTeX](./citations/instant_mesh.txt)
- **SF3D**, Boss et al., 2024 | [Paper](https://arxiv.org/abs/2408.00653) | [Code](https://github.com/Stability-AI/stable-fast-3d) | [BibTeX](./citations/sf3d.txt)
- **Fast3R**, Yang et al., 2025 | [Paper](https://arxiv.org/abs/2501.13928) | [BibTeX](./citations/yang2025fast3r.txt)

#### Latent Generative Models (LGM)

- **Shap-E**, Jun et al., 2023 | [Paper](https://arxiv.org/abs/2305.02463) | [Code](https://github.com/openai/shap-e) | [BibTeX](./citations/shape.txt)
- **3DShape2VecSet**, Zhang et al., SIGGRAPH 2023 | [Paper](https://arxiv.org/abs/2301.11445) | [Code](https://github.com/1zb/3DShape2VecSet) | [BibTeX](./citations/3dShape2VecSet.txt)
- **XCube**, Ren et al., CVPR 2024 | [Paper](https://arxiv.org/abs/2312.03806) | [BibTeX](./citations/xcube.txt)
- **TRELLIS**, Xiang et al., CVPR 2025 | [Paper](https://arxiv.org/abs/2412.01506) | [Code](https://github.com/microsoft/TRELLIS) | [BibTeX](./citations/xiang2025structured.txt)
- **TRELLIS.2**, Xiang et al., 2025 | [Paper](https://arxiv.org/abs/2503.18921) | [Code](https://github.com/microsoft/TRELLIS) | [BibTeX](./citations/xiang2025trellis2.txt)
- **SparseFlex**, He et al., 2025 | [Paper](https://arxiv.org/abs/2503.15448) | [BibTeX](./citations/he2025sparseflex.txt)
- **TripoSG**, Li et al., 2025 | [Paper](https://arxiv.org/abs/2502.06608) | [Code](https://github.com/VAST-AI-Research/TripoSG) | [BibTeX](./citations/li2025triposg.txt)
- **MeshCraft**, He et al., 2025 | [Paper](https://arxiv.org/abs/2503.23022) | [BibTeX](./citations/he2025meshcraft.txt)

#### Part-Aware

- **PAGENet**, Li et al., AAAI 2020 | [BibTeX](./citations/li2020learning.txt)
- **SAMPart3D**, Yang et al., 2024 | [BibTeX](./citations/yang2024sampart3d.txt)
- **HoloPart**, Yang et al., 2025 | [BibTeX](./citations/yang2025holopart.txt)
- **PartGen**, Chen et al., 2025 | [BibTeX](./citations/chen2025partgen.txt)
- **PartCrafter**, Lin et al., 2025 | [BibTeX](./citations/lin2025partcrafter.txt)
- **OmniPart**, Yang et al., 2025 | [BibTeX](./citations/yang2025omnipart.txt)

---

### Topology Generation

#### Indirect Methods (Post-hoc Remeshing)

- **Instant Meshes**, Jakob et al., 2015 | [Code](https://github.com/wjakob/instant-meshes) | [BibTeX](./citations/instant2015field.txt)
- **QuadriFlow**, Huang et al., SGP 2018 | [Paper](https://arxiv.org/abs/1801.07715) | [Code](https://github.com/hjwdzh/QuadriFlow) | [BibTeX](./citations/huang2018quadriflow.txt)
- **NeurCross**, Dong et al., 2025 | [BibTeX](./citations/dong2025neurcross.txt)

#### Direct Methods -- Autoregressive

- **PolyGen**, Nash et al., ICML 2020 | [Paper](https://arxiv.org/abs/2002.10880) | [Code](https://github.com/deepmind/polygen) | [BibTeX](./citations/nash2020polygen.txt)
- **MeshGPT**, Siddiqui et al., ICLR 2024 | [Paper](https://arxiv.org/abs/2311.15475) | [Project](https://nihalsid.github.io/mesh-gpt/) | [BibTeX](./citations/meshgpt.txt)
- **MeshAnything**, Chen et al., 2024 | [Paper](https://arxiv.org/abs/2406.10163) | [Code](https://github.com/buaacyw/MeshAnything) | [BibTeX](./citations/meshAnything.txt)
- **MeshAnything V2**, Chen et al., 2025 | [Paper](https://arxiv.org/abs/2408.02555) | [Code](https://github.com/buaacyw/MeshAnythingV2) | [BibTeX](./citations/MeshAnythingV2.txt)
- **PivotMesh**, Weng et al., 2024 | [Paper](https://arxiv.org/abs/2405.16890) | [BibTeX](./citations/pivotmesh.txt)
- **EdgeRunner**, Tang et al., 2024 | [Paper](https://arxiv.org/abs/2409.18114) | [BibTeX](./citations/edge_runner.txt)
- **QuadGPT**, Liu et al., 2025 | [Paper](https://arxiv.org/abs/2509.21420) | [BibTeX](./citations/liu2025quadgpt.txt)
- **DeepMesh**, Zhao et al., ICCV 2025 | [Paper](https://arxiv.org/abs/2503.15265) | [Code](https://github.com/zhaorw02/DeepMesh) | [BibTeX](./citations/zhao2025deepmesh.txt)
- **Mesh-RFT**, Liu et al., 2025 | [Paper](https://arxiv.org/abs/2505.16761) | [BibTeX](./citations/liu2025mesh.txt)

#### Direct Methods -- Diffusion

- **PolyDiff**, Alliegro et al., ICCV 2023 | [Paper](https://arxiv.org/abs/2312.11417) | [BibTeX](./citations/alliegro2023polydiff.txt)
- **SpaceMesh**, Shen et al., 2024 | [BibTeX](./citations/space_mesh.txt)
- **MeshCraft**, He et al., 2025 | [Paper](https://arxiv.org/abs/2503.23022) | [BibTeX](./citations/he2025meshcraft.txt)

---

### Appearance Generation

#### UV Unwrapping

- **xatlas**, Barber, 2018 | [Code](https://github.com/jpcy/xatlas) | [BibTeX](./citations/xatlas2018.txt)
- **Auto-UV**, Li et al., 2025 | [BibTeX](./citations/li2025auto.txt)
- **Flatten Anything**, Zhang et al., 2024 | [BibTeX](./citations/zhang2024flatten.txt)
- **FlexPara**, Zhao et al., 2025 | [Paper](https://arxiv.org/abs/2504.01894) | [BibTeX](./citations/zhao2025flexpara.txt)
- **PartUV**, Wang et al., 2025 | [BibTeX](./citations/wang2025partuv.txt)
- **ArtUV**, Chen et al., 2025 | [Paper](https://arxiv.org/abs/2504.09914) | [BibTeX](./citations/chen2025artuv.txt)
- **SeamCrafter**, Xu et al., 2025 | [Paper](https://arxiv.org/abs/2504.12256) | [BibTeX](./citations/xu2025seamcrafter.txt)

#### Texture & PBR Material Generation

- **TEXTure**, Richardson et al., SIGGRAPH 2023 | [Paper](https://arxiv.org/abs/2302.01721) | [Code](https://github.com/TEXTurePaper/TEXTurePaper) | [BibTeX](./citations/texture.txt)
- **Text2Tex**, Chen et al., ICCV 2023 | [Paper](https://arxiv.org/abs/2303.11396) | [Code](https://github.com/daveredrum/Text2Tex) | [BibTeX](./citations/text2tex.txt)
- **TexFusion**, Cao et al., 2023 | [BibTeX](./citations/texfusion.txt)
- **Paint3D**, Zeng et al., 2024 | [Paper](https://arxiv.org/abs/2312.13913) | [Code](https://github.com/OpenTexture/Paint3D) | [BibTeX](./citations/paint3d.txt)
- **FlashTex**, Deng et al., 2024 | [BibTeX](./citations/flashtex.txt)
- **TexGen**, Yu et al., 2024 | [BibTeX](./citations/texgaussian.txt)
- **MVPaint**, Cheng et al., 2025 | [Paper](https://arxiv.org/abs/2411.02336) | [BibTeX](./citations/cheng2025mvpaint.txt)
- **MaterialMVP**, He et al., 2025 | [BibTeX](./citations/he2025materialmvp.txt)
- **MaterialAnything**, Huang et al., 2024 | [Paper](https://arxiv.org/abs/2411.15138) | [BibTeX](./citations/huang2024materialanything.txt)
- **Meta 3D AssetGen**, Siddiqui et al., 2024 | [Paper](https://arxiv.org/abs/2407.02445) | [BibTeX](./citations/meta3dAsset.txt)
- **PBR3DGen**, Wei et al., 2025 | [Paper](https://arxiv.org/abs/2504.12836) | [BibTeX](./citations/wei2025pbr3dgenvlmguidedmeshgeneration.txt)

---

## Characters & Avatars

<p align="center">
  <img src="asset/fig_characters.png" width="100%">
</p>

### Structural Priors

- **SMPL**, Loper et al., SIGGRAPH Asia 2015 | [BibTeX](./citations/smpl.txt)
- **SMPL-X**, Pavlakos et al., CVPR 2019 | [BibTeX](./citations/pavlakos2019expressive.txt)
- **FLAME**, Li et al., SIGGRAPH Asia 2017 | [BibTeX](./citations/li2017flame.txt)

### Full-Body Synthesis

#### Parametric Template

- **Tex2Shape**, Alldieck et al., ICCV 2019 | [BibTeX](./citations/alldieck2019tex2shape.txt)
- **CAPE**, Ma et al., CVPR 2020 | [BibTeX](./citations/ma2020learning.txt)
- **ExPose**, Choutas et al., ECCV 2020 | [BibTeX](./citations/choutas2020monocular.txt)
- **STAR**, Osman et al., ECCV 2020 | [BibTeX](./citations/osman2020star.txt)
- **HybrIK**, Li et al., CVPR 2021 | [BibTeX](./citations/li2021hybrik.txt)

#### Implicit / Hybrid

- **PIFu**, Saito et al., ICCV 2019 | [BibTeX](./citations/saito2019pifu.txt)
- **ARCH**, Huang et al., CVPR 2020 | [BibTeX](./citations/huang2020arch.txt)
- **PIFuHD**, Saito et al., CVPR 2020 | [BibTeX](./citations/saito2020pifuhd.txt)
- **PaMIR**, Zheng et al., TPAMI 2021 | [BibTeX](./citations/zheng2021pamir.txt)
- **SMPLicit**, Corona et al., CVPR 2021 | [BibTeX](./citations/smplicit.txt)
- **ICON**, Xiu et al., CVPR 2022 | [BibTeX](./citations/xiu2022icon.txt)
- **gDNA**, Chen et al., ECCV 2022 | [BibTeX](./citations/gdna.txt)
- **ECON**, Xiu et al., CVPR 2023 | [BibTeX](./citations/xiu2023econ.txt)
- **S3F**, Corona et al., ICCV 2023 | [BibTeX](./citations/corona2023structured3d.txt)

#### GAN / Diffusion Generative

- **StylePeople**, Grigorev et al., 2021 | [BibTeX](./citations/grigorev2021stylepeople.txt)
- **AvatarGen**, Zhang et al., 2022 | [BibTeX](./citations/zhang2022avatargen.txt)
- **AvatarCLIP**, Hong et al., SIGGRAPH 2022 | [BibTeX](./citations/hong2022avatarclip.txt)
- **Get3DHuman**, Xiong et al., 2023 | [BibTeX](./citations/get3dhuman.txt)
- **GETAvatar**, Zhang et al., NeurIPS 2023 | [BibTeX](./citations/zhang2023getavatar.txt)
- **AvatarCraft**, Jiang et al., 2023 | [BibTeX](./citations/jiang2023avatarcraft.txt)
- **DreamHuman**, Kolotouros et al., 2023 | [BibTeX](./citations/dreamhuman.txt)
- **ChuPa**, Kim et al., 2023 | [BibTeX](./citations/kim2023chupa.txt)
- **DreamAvatar**, Cao et al., 2024 | [BibTeX](./citations/cao2024dreamavatar.txt)
- **TADA!**, Liao et al., CVPR 2024 | [BibTeX](./citations/tada.txt)

#### Feed-Forward / Real-Time

- **InstantAvatar**, Jiang et al., CVPR 2023 | [BibTeX](./citations/jiang2023instantavatar.txt)
- **SHERF**, Hu et al., 2023 | [BibTeX](./citations/hu2023sherf.txt)
- **Human GS**, Moreau et al., 2024 | [BibTeX](./citations/humangaussian.txt)
- **HUGS**, Kocabas et al., CVPR 2024 | [BibTeX](./citations/kocabas2024hugs.txt)
- **3DGS-Avatar**, Qian et al., 2024 | [BibTeX](./citations/3dgsAvatar.txt)
- **LHM**, Qiu et al., 2025 | [BibTeX](./citations/qiu2025lhm.txt)
- **OmniAvatar**, Gan et al., 2025 | [BibTeX](./citations/gan2025omniavatar.txt)

### Head & Face Synthesis

#### Morphable + Neural

- **i3DMM**, Yenamandra et al., 2021 | [BibTeX](./citations/yenamandra2021i3dmm.txt)
- **NerFace**, Gafni et al., 2021 | [BibTeX](./citations/gafni2021nerface.txt)
- **EG3D**, Chan et al., CVPR 2022 | [BibTeX](./citations/chan2022efficient.txt)
- **NPHM**, Giebenhain et al., 2023 | [BibTeX](./citations/giebenhain2023learning.txt)
- **Next3D**, Sun et al., CVPR 2023 | [BibTeX](./citations/sun2023next3d.txt)
- **PanoHead**, An et al., CVPR 2023 | [BibTeX](./citations/an2023panohead.txt)
- **RODIN**, Wang et al., 2023 | [BibTeX](./citations/rodin.txt)
- **HeadSculpt**, Han et al., 2023 | [BibTeX](./citations/headArtist.txt)

#### Mesh-Anchored Gaussians

- **GaussianAvatars**, Qian et al., CVPR 2024 | [BibTeX](./citations/qian2024gaussianavatars.txt)
- **FlashAvatar**, Xiang et al., 2024 | [BibTeX](./citations/xiang2024flashavatar.txt)
- **MonoGaussianAvatar**, Chen et al., 2024 | [BibTeX](./citations/chen2024monogaussianavatar.txt)
- **RGCA (Relightable)**, Saito et al., 2024 | [BibTeX](./citations/saito2024relightable.txt)

#### Feed-Forward Reconstruction

- **GAGAvatar**, Chu et al., 2024 | [BibTeX](./citations/chu2024generalizable.txt)
- **Arc2Avatar**, Gerogiannis et al., 2025 | [BibTeX](./citations/gerogiannis2025arc2avatar.txt)
- **HRAvatar**, Zhang et al., 2025 | [BibTeX](./citations/zhang2025hravatar.txt)
- **LAM**, He et al., 2025 | [BibTeX](./citations/he2025lam.txt)
- **Avat3r**, Kirschstein et al., 2025 | [BibTeX](./citations/kirschstein2025avat3r.txt)

#### Rendering & Animation

- **SadTalker**, Zhang et al., CVPR 2023 | [BibTeX](./citations/zhang2023sadtalker.txt)
- **TexTalker**, Li et al., 2025 | [BibTeX](./citations/li2025towards.txt)

### Rigging & Skinning

- **RigNet**, Xu et al., SIGGRAPH 2020 | [BibTeX](./citations/xu2020rignet.txt)
- **SkinningNet**, Mosella-Montoro et al., 2022 | [BibTeX](./citations/mosella2022skinningnet.txt)
- **DeePSD**, Bertiche et al., 2021 | [BibTeX](./citations/bertiche2021deepsd.txt)
- *(Note: TADA!, ChuPa, LAM, and HRAvatar also include rigging capabilities -- see above)*

---

## Scenes & Environments

### Layout Generation

- **ATISS**, Paschalidou et al., NeurIPS 2021 | [BibTeX](./citations/atiss.txt)
- **ProcTHOR**, Deitke et al., CVPR 2022 | [BibTeX](./citations/procthor.txt)
- **Pose2Room**, Nie et al., 2022 | [BibTeX](./citations/nie2022pose2room.txt)
- **DiffuScene**, Tang et al., 2024 | [BibTeX](./citations/diffuscene.txt)
- **Holodeck**, Yang et al., CVPR 2024 | [BibTeX](./citations/yang2024holodeck.txt)
- **LayoutGPT**, Feng et al., 2023 | [BibTeX](./citations/feng2023layoutgpt.txt)
- **LLplace**, Yang et al., 2024 | [Paper](https://arxiv.org/abs/2406.03866) | [BibTeX](./citations/yang2024llplace.txt)
- **CityCraft**, Deng et al., 2024 | [Paper](https://arxiv.org/abs/2406.04983) | [BibTeX](./citations/deng2024citycraft.txt)

### Scene Population & Asset Grounding

- **MIME**, Yi et al., 2023 | [BibTeX](./citations/yi2023mime.txt)
- **AnyHome**, Fu et al., 2024 | [BibTeX](./citations/anyhome.txt)
- **Open-Universe**, Aguina-Kang et al., 2024 | [Paper](https://arxiv.org/abs/2403.09675) | [BibTeX](./citations/aguinakang2024openuniverse.txt)
- **SceneCraft**, Hu et al., 2024 | [BibTeX](./citations/hu2024scenecraft.txt)
- **PhyScene**, Yang et al., 2024 | [BibTeX](./citations/yang2024physcene.txt)
- **UnrealLLM**, Tang et al., 2025 | [BibTeX](./citations/tang2025unrealllm.txt)
- **Layout2Scene**, Chen et al., 2025 | [Paper](https://arxiv.org/abs/2501.02519) | [BibTeX](./citations/chen2025layout2scene.txt)
- **3D-GPT**, Sun et al., 2025 | [BibTeX](./citations/3dgpt.txt)
- **PhysGen3D**, Chen et al., 2025 | [BibTeX](./citations/chen2025physgen3d.txt)

### World-Scale Generation

- **Text2Light**, Chen et al., 2022 | [BibTeX](./citations/text2light.txt)
- **Text2Room**, Hollein et al., 2023 | [BibTeX](./citations/text2room.txt)
- **Infinigen**, Raistrick et al., CVPR 2023 | [BibTeX](./citations/raistrick2023infinite.txt)
- **CityDreamer**, Xie et al., 2024 | [BibTeX](./citations/cityDreamer.txt)
- **Infinigen Indoors**, Raistrick et al., 2024 | [BibTeX](./citations/raistrick2024infinigenindoors.txt)
- **LayerPano3D**, Yang et al., 2025 | [BibTeX](./citations/shuaiyang2025layerpano3d.txt)
- **WorldCraft**, Liu et al., 2025 | [Paper](https://arxiv.org/abs/2502.15601) | [BibTeX](./citations/liu2025worldcraft.txt)

---

## Evaluation & Benchmarks

The survey identifies four evaluation dimensions for production-ready 3D generation:

| Dimension | Metrics |
|-----------|---------|
| **Geometric Fidelity** | Chamfer Distance (CD), F-Score, Normal Consistency, Coverage (COV), Minimum Matching Distance (MMD) |
| **Appearance Quality** | PSNR, SSIM, LPIPS, FID, CLIP Score |
| **Asset Usability** | UV distortion, rig quality, engine import success rate, production-readiness score |
| **Scene-Level** | Physical plausibility, traversability, human preference evaluation |

A key finding of this survey is that existing benchmarks systematically overestimate deployment readiness by focusing on geometric and appearance metrics while neglecting asset usability criteria required for interactive applications.

---

## Industry & Companies

| Company | Key Product | Type | Link |
|---------|------------|------|------|
| Tripo AI | Tripo V2.5 | Closed | [tripo3d.ai](https://www.tripo3d.ai/) |
| Tencent | Hunyuan3D | Open + Closed | [3d.hunyuan.tencent.com](https://3d.hunyuan.tencent.com/) |
| ByteDance | MVDream | Open | - |
| Meshy AI | Meshy 5 | Closed | [meshy.ai](https://www.meshy.ai/) |
| Deemos | Rodin Gen 1.5 | Closed | [hyperhuman.deemos.com](https://hyperhuman.deemos.com/) |
| DreamTech | - | Closed | [dreamtech.com](https://www.dreamtech.com/) |
| Luma AI | Genie | Closed | [lumalabs.ai](https://lumalabs.ai/) |
| CSM AI | - | Closed | [csm.ai](https://www.csm.ai/) |
| Stability AI | SF3D | Open | [stability.ai](https://stability.ai/) |
| NVIDIA | Edify 3D | Closed | [build.nvidia.com](https://build.nvidia.com/) |
| SUDO AI | - | Closed | [sudo.ai](https://www.sudo.ai/) |

---

## Citation

If you find this survey useful, please cite our paper:

```bibtex
@article{wu2026production,
  title={From Visual Synthesis to Interactive Worlds: A Survey of Production-Ready 3D Generation},
  author={Wu, Jiafeng and Lou, Zhuofan and Liu, Jian and Du, Dazhao and Guo, Chunchao and Guo, Song},
  journal={ACM Computing Surveys},
  year={2026}
}
```

If you also use resources from the v1 collection, please additionally cite:

```bibtex
@article{liu2023awesome,
  title={Awesome-AIGC-3D: A curated list of AIGC 3D papers},
  author={Liu, Jian},
  journal={GitHub repository},
  year={2023},
  url={https://github.com/hitcslj/Awesome-AIGC-3D}
}
```

---

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

> **Note:** Pull requests should target the **v2** branch. The `main` branch preserves the original v1 awesome list.

---

## Acknowledgments

This work was supported by the Hong Kong University of Science and Technology (HKUST) and Tencent Hunyuan.

---

## v1 Paper Collection

The original awesome list curated by Jian Liu is preserved on the [**main branch**](https://github.com/hitcslj/Awesome-AIGC-3D/tree/main). It contains a broader collection of AIGC 3D papers organized by topic (3D generation, 4D generation, editing, etc.) without the production-pipeline focus of v2.

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=hitcslj/Awesome-AIGC-3D&type=Date)](https://star-history.com/#hitcslj/Awesome-AIGC-3D&Date)
